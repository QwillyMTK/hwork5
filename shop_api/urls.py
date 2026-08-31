from django.urls import path
from product.views import (
    category_list_create, category_detail,
    product_list_create, product_detail,
    review_list_create, review_detail
)

urlpatterns = [
    # категории
    path("api/v1/categories/", category_list_create),
    path("api/v1/categories/<int:pk>/", category_detail),

    # товары
    path("api/v1/products/", product_list_create),
    path("api/v1/products/<int:pk>/", product_detail),

    # отзывы
    path("api/v1/reviews/", review_list_create),
    path("api/v1/reviews/<int:pk>/", review_detail),
]
