from django.urls import path
from .views import (
    category_list_create, category_detail,
    product_list_create, product_detail,
    review_list_create, review_detail
)

urlpatterns = [
    # категории
    path("categories/", category_list_create),
    path("categories/<int:pk>/", category_detail),

    # товары
    path("products/", product_list_create),
    path("products/<int:pk>/", product_detail),

    # отзывы
    path("reviews/", review_list_create),
    path("reviews/<int:pk>/", review_detail),
]
