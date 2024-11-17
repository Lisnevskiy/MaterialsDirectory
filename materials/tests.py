from io import BytesIO

import openpyxl
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Category, Material


class MaterialsAPITestCase(APITestCase):
    def setUp(self):
        # Создаем тестовые категории
        self.category1 = Category.objects.create(name="Category 1", code="CAT001")
        self.category2 = Category.objects.create(name="Category 2", code="CAT002", parent=self.category1)

        # Создаем тестовые материалы
        self.material1 = Material.objects.create(name="Material 1", code="MAT001", cost=100.50, category=self.category1)
        self.material2 = Material.objects.create(name="Material 2", code="MAT002", cost=200.75, category=self.category2)

    def test_upload_xlsx(self):
        # Генерация тестового файла .xlsx
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Materials"
        headers = ["Name", "Code", "Cost", "CategoryCode"]
        sheet.append(headers)
        data = [
            ["Material 3", "MAT003", 150.25, "CAT001"],
            ["Material 4", "MAT004", 300.00, "CAT002"],
        ]
        for row in data:
            sheet.append(row)

        xlsx_file = BytesIO()
        workbook.save(xlsx_file)
        xlsx_file.seek(0)

        # Отправка запроса на загрузку файла
        response = self.client.post(
            "/api/materials/upload/",
            {
                "file": SimpleUploadedFile(
                    "materials.xlsx",
                    xlsx_file.read(),
                    content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                )
            },
            format="multipart",
        )

        # Проверяем статус ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("status", response.data)
        self.assertEqual(response.data["status"], "Загружено")
        self.assertEqual(Material.objects.count(), 4)  # 2 начальных + 2 новых

    def test_tree_view(self):
        # Отправка запроса на дерево категорий
        response = self.client.get("/api/categories/tree/")

        # Проверяем статус ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем структуру дерева
        tree = response.json()
        self.assertEqual(len(tree), 1)  # Один корневой элемент
        root = tree[0]
        self.assertEqual(root["name"], "Category 1")

        # Исправляем ожидаемую сумму
        self.assertEqual(root["total_cost"], 301.25)  # 100.50 (Category 1) + 200.75 (дочерние)
        self.assertEqual(len(root["children"]), 1)  # Одна дочерняя категория

    def test_flat_view(self):
        # Отправка запроса на плоский список категорий
        response = self.client.get("/api/categories/flat/")

        # Проверяем статус ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем содержимое плоского списка
        flat_list = response.json()
        self.assertEqual(len(flat_list), 2)  # Две категории
        self.assertEqual(flat_list[0]["category"], "Category 1")
        self.assertEqual(len(flat_list[0]["materials"]), 1)  # Один материал в Category 1
        self.assertEqual(flat_list[1]["category"], "Category 2")
        self.assertEqual(len(flat_list[1]["materials"]), 1)  # Один материал в Category 2
