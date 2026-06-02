from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('update/<int:pk>',update,name='update')
]