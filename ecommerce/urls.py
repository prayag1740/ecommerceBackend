from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.GetProducts.as_view()),
    path('product/', views.BaseProduct.as_view()),
    path('product/<int:id>', views.BaseProduct.as_view()),

    path('user/', views.User.as_view()),
]
