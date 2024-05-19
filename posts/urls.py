from django.urls import path
from .views import *

urlpatterns = [
    path('', AllFlowersView.as_view(), name='index'),
    path('<str:category_slug>/', AllFlowersView.as_view(), name='category_list'),
]