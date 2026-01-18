from django.db import models

# Create your models here.
# webhook/models.py
from django.db import models

class Client(models.Model):
    phone = models.CharField(max_length=20, unique=True)
    opt_in = models.BooleanField(default=False)

class MessageLog(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    reply_sent = models.BooleanField(default=False)
