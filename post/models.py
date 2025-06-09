from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Post (models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} -> {self.created_at}"
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = 'Посты'