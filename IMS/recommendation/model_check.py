import smart_open
smart_open.open = smart_open.smart_open

import pandas as pd
import numpy as np
from gensim.models import Word2Vec
import random


products = pd.read_csv('./ai_models/products.csv')
model = Word2Vec.load('./ai_models/ims_rec_model.model')

products_dict = products.groupby('product_name')['product_name'].apply(list).to_dict()
print(products_dict)


#Function to obtain all the similar
#products from the similarity vector:
def similar_products(v, n = 30):
    # extract most similar products for the input vector
    if len(v) ==0:
        v = products['product_name'][random.randint(0,50)] # if no buying history, generate random recommendation
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


p_val = ['Optical Mouse', 'samsung earphone', 'Huawei Watch 8', 'Fantech mechanical Keyboard with RGB lights.']
print(model)

similar_prod = similar_products(aggregate_vectors(p_val))
print(similar_prod)