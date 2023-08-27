from django.db import models

# Create your models here.
class Campus(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()


class Coupon(models.Model):
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()