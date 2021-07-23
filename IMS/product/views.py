from .serializers import categorySerializer, subCategorySerializer, productSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import categories, subCategories, products

from ims_users.permissions import adminPermission

from product.pagination import CustomPagination

from rest_framework.views import APIView
from rest_framework.response import Response


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
    permission_classes = (adminPermission,)
    serializer_class = productSerializer


class productListView(generics.ListAPIView):
    queryset = products.objects.all()
    permission_classes = (adminPermission,)
    serializer_class = productSerializer
    pagination_class = CustomPagination


class productUpdateView(generics.UpdateAPIView):
    queryset = products.objects.all()
    permission_classes = (adminPermission,)
    serializer_class = productSerializer
    lookup_field = 'url_slug'


class productDeleteView(generics.DestroyAPIView):
    queryset = products.objects.all()
    permission_classes = (adminPermission,)
    serializer_class = productSerializer
    lookup_field = 'url_slug'


class productDetailView(generics.RetrieveAPIView):
    queryset = products.objects.all()
    permission_classes = (adminPermission,)
    serializer_class = productSerializer
    lookup_field = 'url_slug'

class productSearchView(APIView):
    def get(self,request,url_slug):
        try:
            query = products.objects.filter(url_slug__startswith=url_slug)
            query = [{'url_slug': q.url_slug, 'product_name': q.product_name, 'total_stock': q.total_stock} for q in query]
            return Response(
                {'data': query}
            )
        except:
            return Response({'data': ''})






# List products of the same 
class productListSubCategory(generics.ListAPIView):
    '''def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
'''



