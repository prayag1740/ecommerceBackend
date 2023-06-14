from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.GetProducts.as_view()),
    path('create-product/', views.CreateProduct.as_view())
]
