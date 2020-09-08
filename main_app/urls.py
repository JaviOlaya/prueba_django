from django.urls import path
from . import views

urlpatterns =[
    
    path('inicio/', views.index, name="index"),
    path('', views.login_page,name="login"),
    path('registro/', views.register_page,name="register"),
    path('logout/', views.logout_page, name ="logout"),
]
