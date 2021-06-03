from django.urls import path
from . import views

urlpatterns = [
    path('addcategory/', views.CategoryCreateView.as_view(), name='add-category'),
]