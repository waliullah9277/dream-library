from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tranactions
from django.urls import reverse_lazy
from .forms import DepositeForm
from .constants import DEPOSIT, BORROW_BOOK, RETURN_BOOK
from django.contrib import messages
from datetime import datetime
from django.db.models import Sum
from django.views import View
from admin_posts.models import AdminPost
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Create your views here.

#transactions send email start here
def send_transaction_email(user, amount, subject, template):
    message = render_to_string(template, {
        'user': user,
        'amount': amount,
    })
    to_email = user.email
    send_eamil = EmailMultiAlternatives(subject, ' ', to=[to_email])
    send_eamil.attach_alternative(message, 'text/html')
    send_eamil.send()

#transactions send email end here
    
class TranactionsMixinView(LoginRequiredMixin, CreateView):
    model = Tranactions
    template_name = 'tranactions/tranactions_form.html'
    title = ''
    success_url = reverse_lazy('tranactions_report')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account' : self.request.user.account
        })
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title' : self.title
        })
        return context
    

class DepositMoneyView(TranactionsMixinView):
    form_class = DepositeForm
    title = 'Deposit Money'

    def get_initial(self):
        initial = {'tranaction_type' : DEPOSIT}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount
        account.save(
            update_fields = ['balance']
        )
        messages.success(self.request, f'{amount} $ has been deposit successfully !')
        send_transaction_email(self.request.user, amount, 'Deposit successfully', 'tranactions/deposit_send_email.html')

        return super().form_valid(form)
    
class TransctionReportView(LoginRequiredMixin, ListView):
    template_name = 'tranactions/tranactions_report.html'
    model = Tranactions
    balance = 0

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            account=self.request.user.account
        )

        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')

        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

            queryset = queryset.filter(
                timestamp__date__gte=start_date, timestamp__date__lte=end_date)
            self.balance = Tranactions.objects.filter(
                timestamp__date__gte=start_date, timestamp__date__lte=end_date).aggregate(Sum('amount'))['amount__sum']
        else:
            self.balance = self.request.user.account.balance

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'account': self.request.user.account
        })
        return context


    
