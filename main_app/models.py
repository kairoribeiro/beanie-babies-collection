from django.db import models

# Create your models here.

class Baby(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    image = models.ImageField(blank=True, upload_to='images')
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name