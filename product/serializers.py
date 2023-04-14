from rest_framework import serializers
from product.models import Category, Product, Review
from rest_framework.exceptions import ValidationError


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    products_count = ProductSerializer

    class Meta:
        model = Category
        fields = 'id name products_count'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewStarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars'.split()


class ProductsReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = 'title reviews rating'.split()


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=3, max_length=100)

class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(required=False, default="No description")
    price = serializers.FloatField()
    category_id = serializers.IntegerField()

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExists:
            raise ValidationError('Category not found!')
        return category_id


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=150)
    stars = serializers.IntegerField(required=False, min_value=1, max_value=5)
    product_id = serializers.IntegerField()

    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExists:
            raise ValidationError('Product not found!')
        return product_id
