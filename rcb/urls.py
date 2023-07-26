from django.urls import path

from rcb.views import *
app_name='Bangalore'

urlpatterns=[
    path('virat/',virat,name='virat'),
]