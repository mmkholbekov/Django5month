from django.contrib import admin
from django.urls import path
from product import views
# from .views import category_list,


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categories/', views.category_list_api_view),
    path('api/v1/categories/<int:id>/', views.category_detail_api_view),
    path('api/v1/products/', views.product_list_api_view),
    path('api/v1/products/<int:id>/', views.product_detail_api_view),
    path('api/v1/reviews/', views.review_list_api_view),
    path('api/v1/reviews/<int:id>/', views.review_detail_api_view),
    path('api/v1/products/reviews/', views.products_reviews_api_view),
]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/categories/', views.category_list, name='categories' ),
#     path('api/v1/categories/<int:id>/', views.category_detail, name='category_detail'),
#     path('api/v1/products/', views.product_list, name='product_list'),
#     path('api/v1/products/<int:id>/', views.product_detail, name='product_detail'),
#     path('api/v1/reviews/', views.review_list, name='review_list'),
#     path('api/v1/reviews/<int:id>/', views.review_detail, name='review_detail'),
#     path('api/v1/products/reviews/', views.products_reviews),
# ]
