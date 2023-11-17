from. import  views
from django.urls import path

urlpatterns = [
# path('',views.demo,name='demo'),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('app_form/', views.app_form, name='app_form'),
    path('sucess/', views.sucess, name='sucess'),
    path('logout', views.logout, name='logout'),

]
