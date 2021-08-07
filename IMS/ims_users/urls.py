from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('login/', views.loginView.as_view(), name='obtain_token'),
    path('nlogin/', views.adminTokenObtainPairView.as_view(), name='obtain_token_new'),
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

    # Staff management:
    path('staff/register/', views.staffRegisterView.as_view(), name="staff_register"),
    path('staff/update_profile/<int:pk>/', views.staffProfileUpdate.as_view(), name="staff_profile_update"),
    path('staff/modify_pay/<int:pk>/', views.staffPayView.as_view(), name="staff_profile_update"),
    path('staff/staff_delete/<int:pk>/', views.staffDeleteView.as_view(), name="staff_profile_update"),
    path('staff/stafflist/', views.staffListView.as_view(), name="staff_list"),
    path('staff/staff_payment_list/', views.staffPaymentListView.as_view(), name="staff_list"),
    path('staff/staffdetail/<int:pk>/', views.staffDetailView.as_view(), name="staff_detail"),
    path('staff/paystaff/',views.staffPayRecordView.as_view(), name="staff_pay_record"),
    path('staff/totalMoneyPaidToStaff/',views.totalMoneyPaidToStaff.as_view(), name="staff_payment_analysis"),
    # Customer: 
    path('customer/customerlist/', views.customerListView().as_view(), name="customer_list"),
]
