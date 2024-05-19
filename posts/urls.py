from django.urls import path
from .views import *

urlpatterns = [
    path('', AllFlowersView.as_view(), name='index')
]