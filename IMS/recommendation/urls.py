from django.urls import path
from . import views

urlpatterns = [
    path('<email_slug>/', views.recommend.as_view(), name='recommend'),
]