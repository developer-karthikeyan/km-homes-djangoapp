from django.contrib import admin
from django.urls import path
from . import views
# from .views import UserdefinedPasswordChangeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'),
    name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"),
    name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), 
    name='password_reset_complete'),  
    path('profile/password_change/', views.password_change_request, name='password_change'),
    # path('profile/password_change/', auth_views.PasswordChangeView.as_view(template_name='password/password_change.html'), 
    # name='password_change'),  
    # path('profile/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), 
    # name='password_change_done'), 
    # path('profile/password_change/', UserdefinedPasswordChangeView.as_view(template_name='password/password_change.html'), 
    # name='password_change'),
    path('profile/', views.profile, name='profile'),
]