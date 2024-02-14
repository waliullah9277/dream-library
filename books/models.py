from django.db import models
from django.contrib.auth.models import User
from admin_posts.models import AdminPost

# Create your models here.

class BuyBook(models.Model):
    place_order = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    admin_post = models.ForeignKey(AdminPost, on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.SmallIntegerField(default=0)
    returned = models.BooleanField(default=False, null=True, blank=True)


class BorrowedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    book = models.ForeignKey(AdminPost, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    quantity = models.SmallIntegerField(default=0, null=True, blank=True)
    returend = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.book.book_name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(AdminPost, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return self.user.username