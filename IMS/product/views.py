from django.shortcuts import render
from .serializers import categorySerializer, subCategorySerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import categories, subCategories

from ims_users.permissions import adminPermission


# Create your views here.
class categoryListView(generics.ListAPIView):
    queryset = categories.objects.all()
    permission_classes = (adminPermission,)
    serializer_class = categorySerializer


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


class subCategoryCreateView(generics.CreateAPIView):
    queryset = subCategories.objects.all()
    permission_classes = (adminPermission,)
    serializer_class = subCategorySerializer


class subCategoryListView(generics.ListAPIView):
    queryset = subCategories.objects.all()
    permission_classes = (adminPermission,)
    serializer_class = subCategorySerializer


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
