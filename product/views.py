from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category, Review
from product.serializers import ProductSerializer, CategorySerializer, ReviewSerializer, \
    ProductsReviewsSerializer


@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data="Error! Page not found")
    serializer = CategorySerializer(category)
    return Response(data=serializer.data)


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data="Error! Page not found")
    serializer = ProductSerializer(product)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_list(request):
    review = Review.objects.all()
    serializer = ReviewSerializer(review, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_detail(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data="Error! Page not found")
    serializer = ReviewSerializer(review)
    return Response(data=serializer.data)


@api_view(['GET'])
def products_reviews(request):
    products = Product.objects.all().prefetch_related('reviews')
    serializer = ProductsReviewsSerializer(products, many=True)
    return Response(data=serializer.data)
