from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='obtain_token'),
    path('login/refresh/', TokenRefreshView.as_view(), name="refresh_token"),
    path('test/', views.testView.as_view(), name='test'),
    path('register/', views.registerView.as_view(), name='register'),
    path('change_password/<int:pk>/', views.changePasswordView.as_view(),
        name="change_password"),
    path('update_profile/<int:pk>/', views.updateProfileView.as_view(),
        name="update_profile"),
    path('logout/', views.logoutView.as_view(), name='logout'),
    path('logout_all/', views.logoutAllView.as_view(), name='logout_all'),
    path('adminlogin/', views.adminTokenObtainPairView.as_view(),
        name='admin_obtain_token'),
    path('adminlogin/refresh/', TokenRefreshView.as_view(),
         name="admin_refresh_token"),
]
