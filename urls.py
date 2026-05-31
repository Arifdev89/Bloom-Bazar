from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    # Auth
    path('api/register/', views.RegisterView.as_view(), name='register'),
    path('api/login/', views.LoginView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Categories
    path('api/categories/', views.CategoryListView.as_view(), name='categories'),

    # Products
    path('api/products/', views.ProductListView.as_view(), name='products'),
    path('api/products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),

    # Cart
    path('api/cart/', views.CartView.as_view(), name='cart'),
    path('api/cart/add/', views.AddToCartView.as_view(), name='add-to-cart'),
    path('api/cart/remove/<int:item_id>/', views.RemoveFromCartView.as_view(), name='remove-from-cart'),

    # Orders
    path('api/orders/', views.OrderListView.as_view(), name='orders'),
    path('api/orders/place/', views.PlaceOrderView.as_view(), name='place-order'),
    path('api/orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),

    # Frontend
    path('', views_frontend.home, name='home'),
]
