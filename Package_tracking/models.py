import uuid
from django.db import models

class Package(models.Model):
    STATUS_CHOICES = [
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('in_transit', 'In Transit'),
        ('customs_clearance', 'Customs Clearance'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
    ]

    sender_name = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100)
    receiver_email = models.EmailField()
    tracking_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='processing')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expected_delivery_date = models.DateField(null=True, blank=True)
    delivery_address = models.TextField(blank=True, null=True)
    current_location = models.CharField(max_length=255, null=True, blank=True)
    from_location = models.CharField(max_length=255, null=True, blank=True)
    to_location = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.tracking_id} - {self.receiver_name}"
