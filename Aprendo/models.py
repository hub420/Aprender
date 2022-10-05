from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # muy importante sin este def no se ven los titulos de los topics
    def __str__(self):
        return self.text

class Entry(models.Model):
    """algo especifico aprendido acerca del tema"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Retorna un string representacion del modelo"""
        return f"{self.text[:50]}..."
        #return self.text[:50]+'...'