from rest_framework.permissions import AllowAny, IsAuthenticated
from ims_users.permissions import customerPermission

from product.models import Recipt, products
from product.serializers import productSerializer

# For custom views:
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

# Related to AI model:
import smart_open
smart_open.open = smart_open.smart_open

import pandas as pd
import numpy as np
from gensim.models import Word2Vec
import random

products_df = pd.read_csv('./recommendation/ai_models/products.csv')
model = Word2Vec.load('./recommendation/ai_models/ims_rec_model.model')

products_dict = products_df.groupby('product_name')['product_id'].apply(list).to_dict()
#print(products_dict)


#Function to obtain all the similar
#products from the similarity vector:
def similar_products(v, n = 30):
    # extract most similar products for the input vector
    if len(v) ==0:
        v = products_df['product_name'][random.randint(0,50)] # if no buying history, generate random recommendation
    ms = model.wv.similar_by_vector(v, topn= n+1)[1:]
    
    # extract name and similarity score of the similar products
    new_ms = []
    for j in ms:
        pair = (products_dict[j[0]][0], j[1])
        new_ms.append(pair)
        
    return new_ms    


# Function to average all the vectors of the 
# products the user has bought so far and use 
# the resultant to find similar products:
def aggregate_vectors(products):
    product_vec = []
    for i in products:
        try:
            product_vec.append(model.wv[i])
        except KeyError:
            continue  
    if len(product_vec) == 0:
        return product_vec 
    return np.mean(product_vec, axis=0)


def filter_same_products(similar_prod, p_val):
    for prod in p_val:
        for similar in similar_prod:
             if similar[0] == prod:
                    similar_prod.remove(similar)
    return similar_prod


# p_val = ['Optical Mouse', 'samsung earphone', 'Huawei Watch 8', 'Fantech mechanical Keyboard with RGB lights.']
# print(model)

# similar_prod = similar_products(model.wv['Optical Mouse'])
# print(similar_prod)

class recommend(APIView):
    permission_classes = (AllowAny,)
    def get(self, request,email_slug):

        # Extracting all purchased product
        recipts = Recipt.objects.filter(email=email_slug)
        product_arr = []
        for recipt in recipts:
            recipt_products = recipt.product.all()
            for product in recipt_products:
                product_arr.append(
                    product.product_name
                )

        similar_prod = similar_products(aggregate_vectors(product_arr))
        filtered = filter_same_products(similar_prod, product_arr)
        filtered = filtered[:10]
  
        product_ids = []
        for ids in filtered:
            product_ids.append(ids[0])
        
        recommended_products = products.objects.filter(pk__in=product_ids)
        recommend_serializer = productSerializer(recommended_products, many=True)

        return Response(recommend_serializer.data)
            


