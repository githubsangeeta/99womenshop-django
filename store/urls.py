from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<slug:catagory_slug>/', views.store, name='products_by_catagory'),
    #to create the product details page 
    path('<slug:catagory_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'), 


    # Other URL patterns if any...
]