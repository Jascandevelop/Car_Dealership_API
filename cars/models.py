from django.db import models

class Car(models.Model):
    posted = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=50)
    year = models.IntegerField(null=True)
    miles = models.FloatField(max_length=6, null=True)

    def __str__(self):
        return self.name