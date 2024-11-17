from rest_framework import serializers

from .models import Category, Material


class MaterialSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Material"""

    class Meta:
        model = Material
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Category"""

    class Meta:
        model = Category
        fields = "__all__"
