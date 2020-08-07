from django.urls import path
from .views import *
from .parse import *

urlpatterns = [
    path('', index),
    path('bac', bac),
    path('spec', spec),
    path('mag', mag),
    path('asp', asp),
    path('ord', ordinate),
    path('search', search)
]
