from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer
from common.validators import validate_age_from_token

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # достаём payload из токена
        token_data = getattr(self.request.auth, "payload", {}) or {}
        validate_age_from_token(token_data)
        serializer.save(author=self.request.user)
