from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet, OrderItemViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)

