from rest_framework import serializers

from .models import Author, Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    products = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = Author
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be positive")
        return value

    def validate(self, data):
        title = data.get("title")
        price = data.get("price")

        if title == "apple" and price < 2000:
            raise serializers.ValidationError("This product must be scam")
        return data
