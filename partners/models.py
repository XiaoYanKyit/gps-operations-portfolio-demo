from django.db import models
from django.contrib.auth.models import User


class GPSResetLog(models.Model):

    RESET_TYPES = [
        ("SINGLE", "Single"),
        ("BULK", "Bulk"),
    ]

    STATUS_CHOICES = [
        ("SUCCESS", "Success"),
        ("FAILED", "Failed"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="gps_reset_logs"
    )

    card_code = models.CharField(
        max_length=50
    )

    ship_to_code = models.CharField(
        max_length=100,
        blank=True
    )

    reset_type = models.CharField(
        max_length=20,
        choices=RESET_TYPES
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    message = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f"{self.card_code} - "
            f"{self.status} - "
            f"{self.created_at}"
        )

    class Meta:
        ordering = ["-created_at"]


class OutletRemovalLog(models.Model):

    REMOVAL_TYPES = [
        ("BULK", "Bulk"),
    ]

    STATUS_CHOICES = [
        ("SUCCESS", "Success"),
        ("FAILED", "Failed"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="outlet_removal_logs"
    )

    code = models.CharField(
        max_length=100
    )

    customer_code = models.CharField(
        max_length=100
    )

    removal_type = models.CharField(
        max_length=20,
        choices=REMOVAL_TYPES,
        default="BULK"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    message = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f"{self.code} - "
            f"{self.customer_code} - "
            f"{self.status}"
        )

    class Meta:
        ordering = ["-created_at"]