from django.db import models

class films(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    year=models.IntegerField()
    image=models.ImageField(upload_to='pics')
    def __str__(self):
        return self.name