from django.db import models
# Create your models here.

class ContactMessage(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=255)
    date_time = models.DateField(auto_now_add=False)
    notes = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.full_name
