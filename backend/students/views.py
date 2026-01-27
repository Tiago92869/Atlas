from rest_framework import generics
from .models import Student
from students.serializers import StudentCreateSerializer

class StudentCreateAPIView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer