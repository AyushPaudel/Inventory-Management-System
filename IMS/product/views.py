from re import I
from django.db.models import query
from django.http.response import Http404
from django.utils.timezone import override
from rest_framework import response
from .serializers import categorySerializer, receiptCreateSerializer, recieptObtainSerializer, subCategorySerializer, productSerializer, customerRecordSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from .models import categories, subCategories, products, imsUser, Recipt

from ims_users.permissions import adminPermission, staffPermission, customerPermission

from product.pagination import CustomPagination


# For custom views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers


# Create your views here.


# Category:
class categoryListView(generics.ListAPIView):
    queryset = categories.objects.all()
    permission_classes = (adminPermission,)
    serializer_class = categorySerializer
    pagination_class = CustomPagination


class categoryUpdateView(generics.UpdateAPIView):
    queryset = categories.objects.all()
    permission_classes = (adminPermission,)
    serializer_class = categorySerializer
    lookup_field = 'url_slug'


class categoryDetailView(generics.RetrieveAPIView):
    queryset = categories.objects.all()
    permission_classes = (adminPermission,)
    serializer_class = categorySerializer
    lookup_field = 'url_slug'


class categoryCreateView(generics.CreateAPIView):
    queryset = categories.objects.all()
    permission_classes = (adminPermission,)
    serializer_class = categorySerializer


class categoryDeleteView(generics.DestroyAPIView):
    queryset = categories.objects.all()
    permission_classes = (adminPermission,)
    serializer_class = categorySerializer
    lookup_field = 'url_slug'


# Sub-category:
class subCategoryCreateView(generics.CreateAPIView):
    queryset = subCategories.objects.all()
    permission_classes = (adminPermission,)
    serializer_class = subCategorySerializer


class subCategoryListView(generics.ListAPIView):
    queryset = subCategories.objects.all()
    permission_classes = (adminPermission,)
    serializer_class = subCategorySerializer
    pagination_class = CustomPagination


class subCategoryDetailView(generics.RetrieveAPIView):
    queryset = subCategories.objects.all()
    permission_classes = (adminPermission,)
    serializer_class = subCategorySerializer
    lookup_field = 'url_slug'


class subCategoryUpdateView(generics.UpdateAPIView):
    queryset = subCategories.objects.all()
    permission_classes = (adminPermission,)
    serializer_class = subCategorySerializer
    lookup_field = 'url_slug'


class subCategoryDeleteView(generics.DestroyAPIView):
    queryset = subCategories.objects.all()
    permission_classes = (adminPermission,)
    serializer_class = categorySerializer
    lookup_field = 'url_slug'


# Products:
class productCreateView(generics.CreateAPIView):
    queryset = products.objects.all()
    permission_classes = (adminPermission, staffPermission)
    serializer_class = productSerializer


class productListView(generics.ListAPIView):
    queryset = products.objects.all()
    permission_classes = (adminPermission, staffPermission)
    serializer_class = productSerializer
    pagination_class = CustomPagination


class productUpdateView(generics.UpdateAPIView):
    queryset = products.objects.all()
    permission_classes = (adminPermission, staffPermission)
    serializer_class = productSerializer
    lookup_field = 'url_slug'


class productDeleteView(generics.DestroyAPIView):
    queryset = products.objects.all()
    permission_classes = (adminPermission, staffPermission)
    serializer_class = productSerializer
    lookup_field = 'url_slug'


class productDetailView(generics.RetrieveAPIView):
    queryset = products.objects.all()
    permission_classes = (adminPermission,  staffPermission)
    serializer_class = productSerializer
    lookup_field = 'url_slug'

class receiptViewAll(generics.ListAPIView):
    permission_classes =(AllowAny,)
    queryset = Recipt.objects.all()
    serializer_class = recieptObtainSerializer
class receiptView(generics.RetrieveAPIView):
    permission_classes =(AllowAny,)
    queryset = Recipt.objects.all()
    serializer_class = recieptObtainSerializer
    lookup_field = 'unique_token'

class receiptCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = receiptCreateSerializer
    
class productSearchView(generics.ListAPIView):
    permission_classes = (adminPermission, staffPermission)
    serializer_class = productSerializer
    lookup_url_kwarg="url_slug"

    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_url_kwarg)
        queryset = products.objects.filter(url_slug__startswith=uid)
        return queryset 

class productSearchThroughName(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = productSerializer
    lookup_url_kwarg="url_slug"

    def get_queryset(self):
        print(self.kwargs)
        name = self.kwargs.get(self.lookup_url_kwarg)
        print(name)
        queryset = products.objects.filter(product_name__startswith=name)
        print(queryset)
        return queryset 

# List products of the same sub-category:
class productListSubCategory(generics.ListAPIView):
    permission_classes = (adminPermission, staffPermission)
    serializer_class = productSerializer
    lookup_url_kwarg="url_slug"

    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_url_kwarg)
        queryset = products.objects.filter(url_slug=uid)
        return queryset


# Customer Detail View:
class customerRecordView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = imsUser.objects.filter(user_type='CU')
    serializer_class = customerRecordSerializer


# Redeem token View:
class redeemToken(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, unique_token):
        try: 
            recipt = Recipt.objects.get(unique_token=unique_token)
        except: 
            content = {'message': "Error: Code not valid!!!"}
        else:
            if recipt.redeemed == False:
                recipt.redeemed = True
                recipt.save()
                content = {'message': "Congrats! You redeemed your token", 'Token': f"{recipt.unique_token}", 'id': f"{recipt.id}"}
            else:
                content = {'message': "Error: Code already redeemed!!!", 'Token': f"{recipt.unique_token}", 'id': f"{recipt.id}",}
        return Response(content)


class getIdFromToken(APIView):
    permission_classes = (AllowAny,)
    def get(self,request,token):
        try: 
            recipt = Recipt.objects.get(unique_token=token)
            content = {'message': "Token is valid", 'Token': f"{recipt.unique_token}", 'id': f"{recipt.id}"}
        except: 
            content = {'message': "Error: Code not valid!!!"}
        
        return response(content)


class totalStockAndTotalProfitSoldBySubCategory(APIView):
    permission_classes = (adminPermission,)
    def get(self, request):
        q = subCategories.objects.all()
        print(q)
        sub_arr = []
        for queryset in q:
            print("ok")
            products = queryset.products_set.all()
            total_stock_sold = 0
            tso =0
            total_stock = 0
            total_profit = 0
            sold_amount = 0
            for product in products:
                tso = product.original_stock - product.total_stock
                total_profit += (product.product_max_price - product.product_discount_price) * tso
                sold_amount += (product.product_max_price * tso) 
                total_stock_sold += product.original_stock - product.total_stock
                total_stock += product.original_stock
        
            sub_arr.append({
                'subcategory_name': queryset.title,
                'stock_sold': total_stock_sold,
                'total_stock': total_stock,
                'sold_amount': sold_amount,
                'profit': total_profit,
                })  

        return Response({
            'count': len(sub_arr),
            'results': sub_arr
        })


class totalStockSold(APIView):
    permission_classes = (adminPermission,)
    def get(self, request):
        queryset = products.objects.all()
        total_stock_sold = 0
        total_stock = 0
        for product in queryset:
            total_stock_sold += product.original_stock - product.total_stock
            total_stock += product.original_stock

        return Response({
            'stock_sold': total_stock_sold,
            'total_stock': total_stock
            })


class totalProfit(APIView):
    permission_classes = (adminPermission,)
    def get(self, request):
        queryset = products.objects.all()
        total_profit = 0
        sold_amount = 0
        for product in queryset:
            total_items_sold = product.original_stock - product.total_stock
            total_profit += (product.product_max_price - product.product_discount_price) * total_items_sold
            sold_amount += (product.product_max_price * total_items_sold) 
        return Response({
            'sold_amount': sold_amount,
            'profit': total_profit,
            })


class popularProducts(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        data = []
        queryset = products.objects.all()
        for product in queryset:
             data.append({
                'product': product.product_name,
                'total_stock': product.total_stock,
                'original_stock': product.original_stock
            })
        data.sort(key=lambda x: (x['original_stock']-x['total_stock']),reverse=True)

        return Response({'result': data[:4]})


class popularCategories(APIView):
    def get(self, request):
        data = []
        category_queryset = categories.objects.all()
        final_total = 0
        final_sold = 0
        for category in category_queryset:
            number_of_subcategories = 0
            number_of_products = 0
            total = 0
            sold = 0
            subcategories = category.subcategories_set.all()
            for subcategory in subcategories:
                number_of_subcategories+=1
                products = subcategory.products_set.all()
                for product in products:
                    number_of_products+=1
                    total+=product.original_stock
                    sold+=(product.original_stock-product.total_stock)
            final_total += total    
            final_sold += sold
            data.append({
                'category': category.title,
                'subcategories': number_of_subcategories,
                'product': number_of_products,
                'total': total,
                'sold':sold
            })

        return Response({'result': data , 'total': final_total, 'sold': final_sold})


class CustomersWhoBoughtVariousProducts(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        users = imsUser.objects.all()
        u_arr = []
        for user in users:
            recipts = user.recipt_set.filter(customer=user.id)
            products_arr = []
            for recipt in recipts:
                bought_products = recipt.product.all()
                for product in bought_products:
                    products_arr.append(
                        {
                            "product_name": product.product_name,
                            "url_slug" : product.url_slug,
                            "product_id": product.id
                        }
                    )
            u_arr.append(
                {
                    "username": user.name,
                    "id": user.id,
                    "products": products_arr
                }
            ) 

                
        return Response({'results': u_arr})
