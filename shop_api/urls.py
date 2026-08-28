from django.contrib import admin
from django.urls import path
from product.views import (
    CategoryListView, CategoryDetailView,
    ProductListView, ProductDetailView,
    ReviewListView, ReviewDetailView,
    ProductReviewsListView, CategoryListWithCountView
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # категории
    path("api/v1/categories/", CategoryListView.as_view(), name="categories-list"),
    path("api/v1/categories/<int:pk>/", CategoryDetailView.as_view(), name="categories-detail"),
    path("api/v1/categories/count/", CategoryListWithCountView.as_view(), name="categories-count"),

    # товары
    path("api/v1/products/", ProductListView.as_view(), name="products-list"),
    path("api/v1/products/<int:pk>/", ProductDetailView.as_view(), name="products-detail"),
    path("api/v1/products/reviews/", ProductReviewsListView.as_view(), name="products-reviews"),

    # отзывы
    path("api/v1/reviews/", ReviewListView.as_view(), name="reviews-list"),
    path("api/v1/reviews/<int:pk>/", ReviewDetailView.as_view(), name="reviews-detail"),
]
