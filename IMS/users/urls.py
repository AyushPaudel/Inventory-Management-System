from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path('login/', views.loginView.as_view(), name='obtain_token'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name="refresh_token"),
    path('test/', views.testView.as_view(), name='test'),
    path('register/', views.registerView.as_view(), name='register'),
    path('change_password/<int:pk>/', views.changePasswordView.as_view(), name="change_password"),
    path('update_profile/<int:pk>/', views.updateProfileView.as_view(), name="update_profile")
]
