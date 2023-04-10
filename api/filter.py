from django_filters import rest_framework as filters

from .models import Product


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gt")

    class Meta:
        model = Product
        fields = (
            "title",
            "price",
        )
