from django.contrib import admin
from django.urls import path,include
from .views import DepositMoneyView, TransctionReportView

urlpatterns = [
    path('deposit/', DepositMoneyView.as_view(), name = 'deposit_money'),
    path('tranactions-report/', TransctionReportView.as_view(), name = 'tranactions_report'),
    # path('book-return/<int:book_id>/', ReturnBookView.as_view(), name = 'return_book'),
]