import uuid

from django.conf import settings
from django.db import models

class NotificationType(models.TextChoices):
    TICKET_ASSIGNED = "TICKET_ASSIGNED", "Ticket assigned"
    COMMENT_ADDED = "COMMENT_ADDED", "Comment added"
    MENTION = "MENTION", "Mention"
    STATUS_CHANGED = "STATUS_CHANGED", "Status changed"

class NotificationEntityType(models.TextChoices):
    COMMENT = "COMMENT", "Comment"
    TICKET = "TICKET", "Ticket"

class NotificationSeverity(models.TextChoices):
    INFO = "INFO", "Info"
    WARNING = "WARNING", "Warning"
    CRITICAL = "CRITICAL", "Critical"

class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=200)
    body = models.TextField()
    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)

    type = models.CharField(
        max_length=20,
        choices=NotificationType.choices,
        default=NotificationType.TICKET_ASSIGNED,
        db_index=True,
    )

    entity_type = models.CharField(
        max_length = 10,
        choices=NotificationEntityType.choices,
        default=NotificationEntityType.TICKET,
        db_index=True,
    )

    severity = models.CharField(
        max_length=10,
        choices=NotificationSeverity.choices,
        default=NotificationSeverity.INFO,
        db_index=True,
    )

    ticket = models.ForeignKey(
        "tickets.Ticket",
        on_delete=models.CASCADE,
        related_name="notifications",
    )

    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications_recipient",
    )

    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications_actor",
    )

    class Meta:
        indexes = [
            models.Index(fields=["severity", "type", "entity_type", "-created_at", "is_read"])
        ]

    def __str__(self) -> str:
        return f"#{self.id}: {self.title}"




