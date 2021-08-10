from django.urls import path
from . import views

urlpatterns = [
    path('', views.recommend.as_view(), name='recommend'),
]