from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.app_hello, name = 'app')
]