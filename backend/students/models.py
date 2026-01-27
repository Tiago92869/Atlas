import uuid

from django.db import models

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=225)
    age = models.PositiveIntegerField()

    created_at = models. DateTimeField(auto_now_add=True)
    updated_at = models. DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} {self.age}"
