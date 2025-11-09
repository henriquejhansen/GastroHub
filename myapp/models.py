from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()  # Use DateField para datas
    time = models.TimeField()  # Use TimeField para horas
    people = models.IntegerField()
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.date} {self.time}'
