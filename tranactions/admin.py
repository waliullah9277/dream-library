from django.contrib import admin

from .models import Tranactions

@admin.register(Tranactions)
class TransactinAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount', 'balance_after_tranactions', 'tranaction_type',]

    def save_model(self, request, obj, form, change):
        obj.account.balance += obj.amount
        obj.balance_after_tranactions = obj.account.balance
        obj.account.save()
        super().save_model(request, obj, form, change)
