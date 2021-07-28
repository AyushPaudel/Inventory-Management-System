from django.utils.timezone import override
from .serializers import categorySerializer, subCategorySerializer, productSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import categories, subCategories, products, imsUser, recipt

from ims_users.permissions import adminPermission

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


class productSearchView(generics.ListAPIView):
    permission_classes = (adminPermission,)
    serializer_class = productSerializer
    lookup_url_kwarg="url_slug"

    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_url_kwarg)
        queryset = products.objects.filter(url_slug__startswith=uid)
        return queryset 


# List products of the same sub-category
class productListSubCategory(generics.ListAPIView):
    permission_classes = (adminPermission,)
    serializer_class = productSerializer
    lookup_url_kwarg="url_slug"

    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_url_kwarg)
        queryset = products.objects.filter(url_slug=uid)
        return queryset


# Customer detail and analytics
@APIView(['GET'])
def customerDetail(request, pk):
    






