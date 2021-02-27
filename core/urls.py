from django.urls import path
from .views import item_list, checkout

app_name = 'core'

urlpatterns = [
    path('', item_list, name='item-list'),
    path('checkout/', checkout, name='checkout')

]
