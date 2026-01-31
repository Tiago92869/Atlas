from django.conf import settings
from django.db import models

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_count = models.IntegerField(default=0)
    updated_history = models.JSONField(default=dict)
    updated_by_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name = "updated_by_user",
        null=True,
    )

    deleted_at = models.DateTimeField(null=True)
    deleted_reason = models.TextField(null=True)
    deleted_by_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_index = True,
        related_name = "deleted_by_user",
    )

    ticket_id = models.ForeignKey(
        "tickets.Ticket",
        on_delete=models.SET_NULL,
        related_name = "ticket_id",
    )

    author_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name = "author_id",
    )

    # array of {file_url, file_name, content_type, size_bytes}
    attachments = models.JSONField(default=list)
    attachments_count = models.IntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=["-created_at"]),
        ]

    def __str__(self) -> str:
        return f"#{self.id} {self.body}"
