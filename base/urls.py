from django.urls import path
from base.views import UserProfileListCreateView, userProfileDetailView, ProductList, ProductDetail, OrderList, OrderDetail, OrderItemList, OrderItemDetail

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('order/', OrderList.as_view(), name='product-list'),
    path('order/<int:pk>/', OrderDetail.as_view(), name='product-detail'),
    path('orderItem/', OrderItemList.as_view(), name='product-list'),
    path('orderItem/<int:pk>/', OrderItemDetail.as_view(), name='product-detail'),
    path("all-profiles", UserProfileListCreateView.as_view(), name="all-profiles"),
    path("profile/<int:pk>", userProfileDetailView.as_view(), name="profile"),
]
