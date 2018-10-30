from rest_framework import serializers
from apps.products.models import Product, CatalogItem


class CatalogItemBriefSerializer(serializers.ModelSerializer):

    parent = serializers.SerializerMethodField()

    class Meta:
        model = CatalogItem
        fields = ['id', 'name', 'parent']

    def get_parent(self, obj):
        return {
            "id": obj.parent.id,
            "parent_name": obj.parent.name
        }

class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'status']


class ProductSerializer(serializers.ModelSerializer):
    catalog = CatalogItemBriefSerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'status', 'catalog']
