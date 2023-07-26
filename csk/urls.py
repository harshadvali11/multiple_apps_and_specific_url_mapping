from django.urls import path
app_name='chennai'

from csk.views import *

urlpatterns=[
    path('msd/',msd,name='msd'),
    path('raina/',raina,name='raina'),
    path('jadeja/',jadeja,name='jadeja'),
]