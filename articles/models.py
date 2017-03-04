from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    kind = models.CharField(max_length=20)
    date = models.DateField('published date')
    count = models.IntegerField(default=0)
    content = models.TextField()
    
    def __str__(self):
        return self.title
