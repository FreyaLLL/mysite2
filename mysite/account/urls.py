from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "account"

urlpatterns = [
    #path('login/',views.user_login,name='user_login'),
    path('login/',auth_views.LoginView.as_view(template_name='account/login3.html'),name='user_login'),
    #基于类的方式auth_views.LoginView.as_view()

    path('logout/',auth_views.LogoutView.as_view(template_name='account/logout.html'),name='user_logout'),
    path('register/',views.register,name='user_register'),
]