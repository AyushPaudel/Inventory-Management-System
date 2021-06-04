from django.urls import path
from . import views

urlpatterns = [
    path('addcategory/', views.categoryCreateView.as_view(), name='add-category'),
    path('categoryupdate/<url_slug>/', views.categoryUpdateView.as_view(), name='update-category'),
    path('categorylist/', views.categoryListView.as_view(), name='category-list'),
    path('categorydetail/<url_slug>/', views.categoryDetailView.as_view(), name='category-detail'),
    path('addsubcategory/', views.subCategoryCreateView.as_view(), name='add-subcategory'),
    path('subcategoryupdate/<int:pk>/', views.subCategoryUpdateView.as_view(), name='update-subcategory'),
]

