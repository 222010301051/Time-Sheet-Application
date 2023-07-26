from django.urls import path
from . import views


urlpatterns = [
    path('', views.att, name="att"),
    path('attendance/', views.att, name="atte"),
    path('dashboard/<int:pk>/', views.dash, name="dash"),
    path('submit_attendance/', views.submit_attendance, name='submit_attendance'),
    path('logval/', views.login_val, name="login_val"),
    path('attendance_table/',views.attendance_table, name="attendance_table"),
    ]