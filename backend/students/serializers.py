from rest_framework import serializers
from students.models import Student

class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "age"]
        read_only_fields = ["id"]

    def validate_age(self, value: int) -> int:
        if value < 0:
            raise serializers.ValidationError("Age must be a positive number.")
        if value > 150:
            raise serializers.ValidationError("Age is unrealistically high.")
        return value
