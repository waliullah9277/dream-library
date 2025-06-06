from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from admin_posts.models import AdminPost
from categories.models import CategoryModel
# Create your views here.

def HomeView(request):
    data = AdminPost.objects.all()
    book_categorys = CategoryModel.objects.all()
    return render(request,'index.html', {'data': data,'book_category': book_categorys})


def home(request, category_name_slug=None):
    data = AdminPost.objects.all()
    if category_name_slug is not None:
        book_category = CategoryModel.objects.get(slug = category_name_slug)
        data = AdminPost.objects.filter(book_category = book_category)
    book_categorys = CategoryModel.objects.all()
    return render(request,'index.html', {'data': data, 'book_category': book_categorys})
