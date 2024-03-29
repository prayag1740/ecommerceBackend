from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.GetProducts.as_view()),
    path('product/', views.BaseProduct.as_view()),
    path('product/<int:id>', views.BaseProduct.as_view()),

    path('user/', views.User.as_view()),
    path('user/<int:id>', views.User.as_view()),
    path('login/', views.LoginUser.as_view()),
    path('logout/', views.LogoutUser.as_view()),
]
