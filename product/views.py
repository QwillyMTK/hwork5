from django.db.models import Avg, Count
from rest_framework import generics
from .models import Category, Product, Review
from .serializers import (
    CategorySerializer, ProductSerializer, ReviewSerializer,
    ProductWithReviewsSerializer, CategoryWithCountSerializer
)

# список категорий
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# одна категория
class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# список товаров
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# один товар
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# список отзывов
class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# один отзыв
class ReviewDetailView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# список товаров с отзывами и средним рейтингом
class ProductReviewsListView(generics.ListAPIView):
    serializer_class = ProductWithReviewsSerializer

    def get_queryset(self):
        return Product.objects.annotate(rating=Avg("reviews__stars"))

# список категорий с количеством товаров
class CategoryListWithCountView(generics.ListAPIView):
    serializer_class = CategoryWithCountSerializer

    def get_queryset(self):
        return Category.objects.annotate(products_count=Count("products"))
