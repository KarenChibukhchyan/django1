from django.urls import path
from .views import *

urlpatterns = [
    path('', plot_graphic),
]