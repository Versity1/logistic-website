from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Package

@receiver(post_save, sender=Package)
def send_package_notification(sender, instance, created, **kwargs):
    subject = f"Update on your package with Tracking ID {instance.tracking_id}"
    if created:
        message = f"Dear {instance.receiver_name},\n\nYour package has been created and is currently being processed.\nYour tracking ID is {instance.tracking_id}."
    else:
        message = f"Dear {instance.receiver_name},\n\nThe status of your package with Tracking ID {instance.tracking_id} has been updated to {instance.get_status_display()}."
    
    send_mail(
        subject,
        message,
        'nonyelurichard95@gmail.com.com',
        [instance.receiver_email],
        fail_silently=False,
    )
