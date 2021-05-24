from django.shortcuts import render
from .serializers import addCategory
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import categories


# Create your views here.
class categoryView(generics.CreateAPIView):
    queryset = categories.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = addCategory