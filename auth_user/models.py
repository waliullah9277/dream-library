from django.db import models
from django.contrib.auth.models import User
from .constants import GENDER_TYPE

# Create your models here.

class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE, null = True, blank = True)
    account_no = models.IntegerField()
    birth_date = models.DateField()
    gender = models.CharField(max_length=15, choices = GENDER_TYPE)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places= 2)

    def __str__(self):
        return str(self.account_no)
    
class UserAddress(models.Model):
    user = models.OneToOneField(User, related_name='address', on_delete=models.CASCADE, null=True, blank=True)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.user.email

