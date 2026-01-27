from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from students.models import Student

class StudentCreateAPITests(APITestCase):
    def test_create_student_success(self):
        url = "/api/students/"
        payload = {"name": "Amina", "age": 22}

        response = self.client.post(url, data=payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data["name"], "Amina")
        self.assertEqual(response.data["age"], 22)
        self.assertIn("id", response.data)

        self.assertEqual(Student.objects.count(), 1)
        student = Student.objects.first()
        self.assertEqual(student.name, "Amina")
        self.assertEqual(student.age, 22)

    def test_create_student_invalid_age(self):
        url = "/api/students/"
        payload = {"name": "Amina", "age": -5}

        response = self.client.post(url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("age", response.data)
        self.assertEqual(Student.objects.count(), 0)

    def test_create_student_missing_name(self):
        url = "/api/students/"
        payload = {"age": 22}

        response = self.client.post(url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("name", response.data)
