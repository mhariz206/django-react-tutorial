from django.db import models

# Create your models here.


# added
class Todo(models.Model):
    title = models.CharField(max_length=120) # title
    description = models.TextField() # description
    completed = models.BooleanField(default=False) # completed


    def __str__(self):
        return self.title