from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField() 
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail",args = [str(self.id)])

    