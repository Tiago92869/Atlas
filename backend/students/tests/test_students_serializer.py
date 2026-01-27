from django.test import TestCase
from students.serializers import StudentCreateSerializer

class StudentCreateSerializerTests(TestCase):
    def test_valid_data_is_valid(self):
        data = {"name": "Amina", "age": 22}
        serializer = StudentCreateSerializer(data=data)

        self.assertTrue(serializer.is_valid(), serializer.errors)

    def test_negative_age_is_invalid(self):
        data = {"name": "Amina", "age": -1}
        serializer = StudentCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("age", serializer.errors)

    def test_big_age_is_invalid(self):
        data = {"name": "Amina", "age": 200}
        serializer = StudentCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("age", serializer.errors)