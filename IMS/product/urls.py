from django.urls import path
from . import views

urlpatterns = [
    path('addcategory/', views.categoryCreateView.as_view(), name='add-category'),
    #path('updatecategory/<int:pk>/', views.categoryUpdateView.as_view(), name='update-category'),
    path('addsubcategory/', views.subCategoryCreateView.as_view(), name='add-subcategory'),
    #path('updatesubcategory/<int:pk>/', views.subCategoryUpdateView.as_view(), name='update-subcategory'),
]

