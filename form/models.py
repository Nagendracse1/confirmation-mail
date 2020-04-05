from django.db import models

# Create your models here.
class Detail(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=13)
    how_hear = models.CharField(max_length=20)

    def __str__(self):
        return self.name