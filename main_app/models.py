from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Photo(models.Model):
  title = models.CharField(max_length=255)
  document = models.FileField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
 
  class Meta:
    verbose_name_plural = 'Photos'

  def __str__(self):
    return f"Photo url: {self.url}"