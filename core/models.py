from django.db import models

# Create your models here.
from django.db import models
from .utils import encrypt_message, decrypt_message

class Group(models.Model):
    group_id = models.CharField(max_length=6, unique=True)
    topic = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Group {self.group_id} - {self.topic}"

class Message(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    content = models.TextField()
    anon_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.content = encrypt_message(self.content)
        super().save(*args, **kwargs)

    def get_decrypted_content(self):
        return decrypt_message(self.content)