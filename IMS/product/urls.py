from django.urls import path
from . import views

urlpatterns = [
    #Category
    path('addcategory/', views.categoryCreateView.as_view(), name='add-category'),
    path('categoryupdate/<url_slug>/', views.categoryUpdateView.as_view(), name='update-category'),
    path('categorylist/', views.categoryListView.as_view(), name='category-list'),
    path('categorydetail/<url_slug>/', views.categoryDetailView.as_view(), name='category-detail'),
    path('categorydelete/<url_slug>/', views.categoryDeleteView.as_view(), name='category-delete'),

    #sub-category
    path('addsubcategory/', views.subCategoryCreateView.as_view(), name='add-subcategory'),
    path('subcategoryupdate/<url_slug>/', views.subCategoryUpdateView.as_view(), name='update-subcategory'),
    path('subcategorydetail/<url_slug>/', views.subCategoryDetailView.as_view(), name='subcategory-detail'),
    path('subcategorylist/', views.subCategoryListView.as_view(), name='subcategory-list'),
    path('subcategorydelete/<url_slug>/', views.subCategoryDeleteView.as_view(), name='subcategory-delete'),

    #Products
    path('addproduct/', views.productCreateView.as_view(), name='add-product'),
    path('productlist/', views.productListView.as_view(), name='product-list'),
    path('productupdate/<url_slug>/', views.productUpdateView.as_view(), name='product-update'),
    path('productdetail/<url_slug>/', views.productUpdateView.as_view(), name='product-detail'),
    path('productdelete/<url_slug>/', views.productDeleteView.as_view(), name='product-delete'),
    path('productlist/<url_slug>/', views.productListSubCategory.as_view(), name='product-list-sub'),
    # product search
    path('productSearch/<url_slug>/', views.productSearchView.as_view(),name='product-search'),
    path('search/<url_slug>/', views.productSearchThroughName.as_view(),name='product-search-through-name'),
    # Customer records:
    path('customerrecord/<int:pk>/', views.customerRecordView.as_view(), name='customer-record'),
    # Receipts
    path('receipt/<unique_token>/', views.receiptView.as_view(), name='receipt'),
    path('receipt/', views.receiptViewAll.as_view(), name='receipt'),
    path('createReceipt/', views.receiptCreate.as_view(), name='receipt_create'),
    path('popularProducts/', views.popularProducts.as_view(), name='popular products'),
    path('popularCategories/', views.popularCategories.as_view(), name='popular Categories'),

    path('totalStock/', views.totalStockSold.as_view(), name='popular Categories'),
    path('totalStockBySubCategory/<int:subcategory_id>/', views.totalStockSoldBySubCategory.as_view(), name='popular Categories'),
    path('totalProfit/', views.totalProfit.as_view(), name='popular Categories'),
    path('totalProfitBySubCategory/<int:subcategory_id>/', views.totalProfitBySubCategory.as_view(), name='popular Categories'),

    # Redeem Code:
    path('redeem/<unique_token>/', views.redeemToken.as_view(), name='redeem'),
    path('viewToken/<unique_token>/', views.redeemToken.as_view(), name='redeem'),
]

