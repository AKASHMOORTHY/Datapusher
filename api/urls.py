from django.urls import path
from api.views import RegisterView, LoginView, AdminOnlyView, EmployeeOnlyView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("admin/dashboard/", AdminOnlyView.as_view(), name="admin-dashboard"),
    path("employee/profile/<int:pk>/", EmployeeOnlyView.as_view(), name="employee-profile"),

]
