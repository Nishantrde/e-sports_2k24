from django.urls import path
from .views import *
    
app_name = 'mainapp'

urlpatterns = [
    path('',index, name="log"),
    path('login',log_in),
]


