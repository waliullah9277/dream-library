from django.contrib.auth.forms import UserCreationForm
from .constants import GENDER_TYPE
from django import forms
from django.contrib.auth.models import User
from .models import UserAccount, UserAddress

class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    street_address = forms.CharField(max_length=200)
    city = forms.CharField(max_length=200)
    country = forms.CharField(max_length=200)
    postal_code = forms.IntegerField()
    class Meta:
        model = User
        fields = [
            'username','first_name', 'last_name', 'email', 'password1', 'password2', 'birth_date', 'gender', 'street_address', 'city', 'country', 'postal_code',
        ]


    def save(self, commit=True):
        our_user = super().save(commit=False)
        if commit==True:
            our_user.save()
            birth_date = self.cleaned_data.get('birth_date')
            gender = self.cleaned_data.get('gender')
            street_address = self.cleaned_data.get('street_address')
            city = self.cleaned_data.get('city')
            country = self.cleaned_data.get('country')
            postal_code = self.cleaned_data.get('postal_code')

            UserAccount.objects.create(
                user = our_user,
                gender = gender,
                birth_date = birth_date,
                account_no = 1000+our_user.id,
            )

            UserAddress.objects.create(
                user = our_user,
                street_address = street_address,
                city = city,
                country = country,
                postal_code = postal_code,
            )
            return our_user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
                self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })
                     

class UserUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    street_address = forms.CharField(max_length=200)
    city = forms.CharField(max_length=200)
    country = forms.CharField(max_length=200)
    postal_code = forms.IntegerField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })

        if self.instance:
            try:
                user_account = self.instance.account
                user_address = self.instance.address
            except UserAccount.DoesNotExist:
                user_account = None
                user_address = None

            if user_account:
                self.fields['birth_date'].initial = user_account.birth_date
                self.fields['gender'].initial = user_account.gender
                self.fields['street_address'].initial = user_address.street_address
                self.fields['city'].initial = user_address.city
                self.fields['country'].initial = user_address.country
                self.fields['postal_code'].initial = user_address.postal_code

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

            user_account, created = UserAccount.objects.get_or_create(user=user)
            user_address, created = UserAddress.objects.get_or_create(user=user)

            user_account.birth_date = self.cleaned_data['birth_date']
            user_account.gender = self.cleaned_data['gender']
            user_account.save()

            user_address.street_address = self.cleaned_data['street_address']
            user_address.city = self.cleaned_data['city']
            user_address.postal_code = self.cleaned_data['postal_code']
            user_address.country = self.cleaned_data['country']
            user_address.save()
        return user
                    
    
