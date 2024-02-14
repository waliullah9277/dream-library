from django.contrib import admin
from .models import BuyBook, BorrowedBook, Review

# Register your models here.
admin.site.register(BuyBook)
admin.site.register(BorrowedBook)
admin.site.register(Review)
