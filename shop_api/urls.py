from django.urls import path, include
from product import views


urlpatterns = [
    path('api/v1/products/', views.ProductListAPIView.as_view()),
    path('api/v1/products/<int:id>/', views.ProductDetailAPIView.as_view()),
    path('api/v1/products/reviews/', views.RatingAPIView.as_view()),

    path('api/v1/categories/', views.CategoryListAPIView.as_view()),
    path('api/v1/categories/<int:id>/', views.CategoryDetailAPIView.as_view()),

    path('api/v1/reviews/', views.ReviewListAPIView.as_view()),
    path('api/v1/reviews/<int:id>/', views.ReviewDetailAPIView.as_view()),

    path('api/v1/users/', include('users.urls'))
]
