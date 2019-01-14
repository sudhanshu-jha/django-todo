from django.db import models

# Create your models here.


class Todo(models.Model):
    Serial = models.IntegerField(default=0)
    Title = models.CharField(max_length=200)
    Description = models.TextField(max_length=200)

    def __str__(self):
        return self.Title
