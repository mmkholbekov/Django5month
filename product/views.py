from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category, Review
from .serializers import ProductSerializer, CategorySerializer, ReviewSerializer


@api_view(['GET'])
def category_api_view(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data="ERROR! Такой страницы не существует")
    serializer = CategorySerializer(category)
    return Response(data=serializer.data)


@api_view(['GET'])
def products_api_view(requests):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def products_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data="ERROR! Такой страницы не существует")
    serializer = ProductSerializer(product)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_api_view(request):
    review = Review.objects.all()
    serializer = ReviewSerializer(review, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data="ERROR! Тако страницы не существует")
    serializer = ReviewSerializer(review)
    return Response(data=serializer.data)
