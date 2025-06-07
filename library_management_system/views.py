from django.shortcuts import render
from admin_posts.models import AdminPost
from categories.models import CategoryModel
from django.db.models import Q

# def search_posts(request):
#     query = request.GET.get('q')
#     if query:
#         book_name_query = Q(book_name__icontains=query)
#         book_categories_query = Q(book_category__category_name__icontains=query)

#         search = AdminPost.objects.filter(book_name_query | book_categories_query).distinct()
#     else:
#         search = AdminPost.objects.all()
#     categories = CategoryModel.objects.all()
#     return render(request, 'index.html', {'data': search, 'categories': categories})

def search_posts(request):
    query = request.GET.get('q')
    if query:
        book_name_query = Q(book_name__icontains=query)
        book_categories_query = Q(book_category__category_name__icontains=query)
        search = AdminPost.objects.filter(book_name_query | book_categories_query).distinct()
    else:
        search = AdminPost.objects.all()

    categories = CategoryModel.objects.all()

    return render(request, 'index.html', {
        'data': search,
        'book_category': categories  
    })

