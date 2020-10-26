from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

MECHANICAL = 1
AUTOMATIC = 2
ROBOT = 3
GEARBOX_CHOICES = [(MECHANICAL, 'Механика'), (AUTOMATIC, 'Автомат'), (ROBOT, 'Робот')]
class Car(models.Model):
    manufacturer = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    year = models.IntegerField(validators=[
                                    MaxValueValidator(2200),
                                    MinValueValidator(1768)
                                ])
    gearbox = models.SmallIntegerField(choices=GEARBOX_CHOICES, default=MECHANICAL)
    color = models.CharField('цвет', max_length = 7, default = "#0000ff", blank = True)

    def __str__(self):
        return f'{self.manufacturer} {self.car_model}'
