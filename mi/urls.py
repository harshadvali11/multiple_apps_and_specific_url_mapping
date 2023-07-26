from django.urls import path
from mi.views import *
app_name='mumbai'

urlpatterns=[
    path('rohit/',rohit,name='rohit'),
]