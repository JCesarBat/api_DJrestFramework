from django.db import models
class Project(models.Model):
        title=models.CharField(max_length=100)
        description=models.TextField()
        technology=models.CharField(max_length=100)
        created=models.DateTimeField(auto_now_add=True)
        
# Create your models here.
