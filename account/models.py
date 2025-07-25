from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is User', default=False)
    # is_employee = models.BooleanField('Is employee', default=False)




class Enquiry(models.Model):
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    longitude = models.FloatField()
    latitude = models.FloatField()
    image = models.ImageField(upload_to='enquiry_images')
    ecSocket = models.CharField(max_length=10, choices=(('Good', 'Good'), ('Average', 'Average'), ('Bad', 'Bad')), default='Good')
    boxCondition = models.CharField(max_length=10, choices=(('Good', 'Good'), ('Average', 'Average'), ('Bad', 'Bad')), default='Good')
    loopResistance = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


