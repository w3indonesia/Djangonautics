from django.urls import path
from . import views

urlpatterns = [
    path('', views.under_construction, name='bootcamp_home'),
]
