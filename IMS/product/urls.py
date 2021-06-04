from django.urls import path
from . import views

urlpatterns = [
    #Category
    path('addcategory/', views.categoryCreateView.as_view(), name='add-category'),
    path('categoryupdate/<url_slug>/', views.categoryUpdateView.as_view(), name='update-category'),
    path('categorylist/', views.categoryListView.as_view(), name='category-list'),
    path('categorydetail/<url_slug>/', views.categoryDetailView.as_view(), name='category-detail'),

    #sub-category
    path('addsubcategory/', views.subCategoryCreateView.as_view(), name='add-subcategory'),
    path('subcategoryupdate/<url_slug>/', views.subCategoryUpdateView.as_view(), name='update-subcategory'),
    path('subcategorydetail/<url_slug>/', views.subCategoryDetailView.as_view(), name='subcategory-detail'),
    path('subcategorylist/', views.subCategoryListView.as_view(), name='subcategory-list'),
]

