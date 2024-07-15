from django.urls import path
from . import views

app_name = 'e_commerce'

urlpatterns = [
path('product_list',views.product_list, name='product_list'),

]
