from django.db import models


class Category(models.Model):
    """Модель для категорий материалов"""

    name = models.CharField(max_length=255)
    """Название категории"""
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    """Ссылка на родительскую категорию, может быть пустой для корневых категорий"""
    code = models.CharField(max_length=50, unique=True)
    """Уникальный код категории"""

    def __str__(self):
        return self.name


class Material(models.Model):
    """Модель для материалов"""

    name = models.CharField(max_length=255)
    """Название материала"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="materials")
    """Ссылка на категорию, к которой принадлежит материал"""
    code = models.CharField(max_length=50, unique=True)
    """Уникальный код материала"""
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    """Стоимость материала"""

    def __str__(self):
        return self.name
