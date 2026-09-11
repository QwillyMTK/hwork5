from django.urls import path
from .views import (
    CategoryListCreateView, CategoryDetailView,
    ProductListCreateView, ProductDetailView,
    ReviewListCreateView, ReviewDetailView
)

urlpatterns = [
    # категории
    path("categories/", CategoryListCreateView.as_view()),
    path("categories/<int:pk>/", CategoryDetailView.as_view()),

    # товары
    path("products/", ProductListCreateView.as_view()),
    path("products/<int:pk>/", ProductDetailView.as_view()),

    # отзывы
    path("reviews/", ReviewListCreateView.as_view()),
    path("reviews/<int:pk>/", ReviewDetailView.as_view()),
]
