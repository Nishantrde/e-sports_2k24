from django.urls import path
from .views import *   

urlpatterns = [
    path('', index, name="log"),
    path('thanks/<str:team>', thanks)
]


