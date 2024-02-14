from django import forms
from .models import Tranactions

class TranactionForm(forms.ModelForm):
    class Meta:
        model = Tranactions
        fields = [
            'amount', 'tranaction_type',
        ]

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account')
        super().__init__(*args, **kwargs)
        self.fields['tranaction_type'].disabled = True
        self.fields['tranaction_type'].widget = forms.HiddenInput

    def save(self, commit=True):
        self.instance.account = self.account
        self.instance.balance_after_tranactions = self.account.balance
        return super().save()
    
class DepositeForm(TranactionForm):
    def clean_amount(self):
        min_deposite_amount = 100
        amount = self.cleaned_data.get('amount')
        if amount < min_deposite_amount:
            print(amount)
            raise forms.ValidationError(
                f'You need to deposite at least {min_deposite_amount} $'
            )
        return amount


