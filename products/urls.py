from django.urls import path
from .views import ProductViewSet,ProductUpdateAPIView

urlpatterns = [
    path('', ProductViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('',ProductUpdateAPIView.as_view({'put': 'update', 'patch': 'partial_update'}))
]