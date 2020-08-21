from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('createuser', views.createuser, name='createuser'),
    path('loginview/', views.loginview, name='loginview'),
    path('request_login', views.request_login, name='request_login'),
    path('handlelogout/', views.handlelogout, name='handlelogout'),    
]
