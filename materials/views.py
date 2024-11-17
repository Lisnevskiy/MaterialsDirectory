from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Material
from .serializers import CategorySerializer, MaterialSerializer


class MaterialViewSet(viewsets.ModelViewSet):
    """ViewSet для управления материалами"""

    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

    @action(detail=False, methods=["post"])
    def upload(self, request):
        """Загрузка материалов из файла .xlsx"""

        import openpyxl

        file = request.FILES["file"]
        workbook = openpyxl.load_workbook(file)
        sheet = workbook.active

        materials = []
        for row in sheet.iter_rows(min_row=2, values_only=True):
            material = Material(name=row[0], code=row[1], cost=row[2], category=Category.objects.get(code=row[3]))
            materials.append(material)
        Material.objects.bulk_create(materials)
        return Response({"status": "Загружено"})


class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet для управления категориями материалов"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=False, methods=["get"])
    def flat(self, request):
        """Получение плоского списка категорий"""

        categories = Category.objects.prefetch_related("materials").all()
        data = [{"category": cat.name, "materials": [mat.name for mat in cat.materials.all()]} for cat in categories]
        return Response(data)

    @action(detail=False, methods=["get"])
    def tree(self, request):
        """Получение дерева категорий"""

        def build_tree(category):
            """Рекурсивная функция для построения дерева категорий"""

            children = category.children.all()
            materials = category.materials.all()
            cost = sum(mat.cost for mat in materials) + sum(build_tree(child)["total_cost"] for child in children)
            return {
                "name": category.name,
                "materials": [mat.name for mat in materials],
                "children": [build_tree(child) for child in children],
                "total_cost": cost,
            }

        root_categories = Category.objects.filter(parent__isnull=True)
        data = [build_tree(cat) for cat in root_categories]
        return Response(data)
