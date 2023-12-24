from django.urls import path, include
from . import views
urlpatterns = [
    path("",views.index,name='Home'),
    path("delete/<id>/",views.delete, name='Delete'),
    path("edit/<id>/",views.edit, name='Edit'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout')
]