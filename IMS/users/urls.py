from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='obtain_token'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name="refresh_token"),
    path('test/', views.testView.as_view(), name='test'),
]
