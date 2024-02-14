from django.db import models
from categories.models import CategoryModel
# Create your models here.
class AdminPost(models.Model):
    image = models.ImageField(upload_to='admin_posts/media/uploads/')
    book_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    quantity = models.IntegerField()
    borrow_price = models.DecimalField(max_digits=12, decimal_places=2)
    book_category = models.ManyToManyField(CategoryModel)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.book_name