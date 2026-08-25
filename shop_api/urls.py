from django.contrib import admin
from django.urls import path
from product.views import (
    CategoryListView, CategoryDetailView,
    ProductListView, ProductDetailView,
    ReviewListView, ReviewDetailView
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/categories/", CategoryListView.as_view()),
    path("api/v1/categories/<int:pk>/", CategoryDetailView.as_view()),
    path("api/v1/products/", ProductListView.as_view()),
    path("api/v1/products/<int:pk>/", ProductDetailView.as_view()),
    path("api/v1/reviews/", ReviewListView.as_view()),
    path("api/v1/reviews/<int:pk>/", ReviewDetailView.as_view()),
]
