from django.db import models
from auth_user.models import UserAccount, User
from .constants import TRANACTION_TYPE
from admin_posts.models import AdminPost
# Create your models here.

class Tranactions(models.Model):
    account = models.ForeignKey(UserAccount, related_name="transactions", on_delete=models.CASCADE, null= True, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    balance_after_tranactions = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    tranaction_type = models.IntegerField(choices=TRANACTION_TYPE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(AdminPost, on_delete=models.CASCADE, null=True, blank=True)
    returned = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']


