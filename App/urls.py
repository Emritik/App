from django.contrib import admin
from django.urls import path, include
from Todo_App.views import SignupView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Todo_App.urls')),
    path('signup/',SignupView.as_view(),name='signup'),

]
