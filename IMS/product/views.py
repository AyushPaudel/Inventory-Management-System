from django.shortcuts import render
from .serializers import addCategory, addSubCategory
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import categories, subCategories


# Create your views here.
class CategoryCreateView(generics.CreateAPIView):
    queryset = categories.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = addCategory

class CategoryUpdateView(generics.UpdateAPIView):
    queryset = categories.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = addCategory


class SubCategoryCreateView(generics.CreateAPIView):
    queryset = subCategories.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = addSubCategory

class SubCategoryUpdateView(generics.UpdateAPIView):
    queryset = subCategories.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = addSubCategory