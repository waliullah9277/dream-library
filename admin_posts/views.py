from django.shortcuts import render, get_object_or_404,redirect
from .models import AdminPost
from django.views.generic import DetailView
from books.models import Review
from django.contrib import messages
# Create your views here.


def post_details(request, id):
    if request.method == 'GET':
        try:
            book = AdminPost.objects.get(id=id)
            reviews = Review.objects.filter(book=book)  # sob review
            review_count = reviews.count()
            return render(request, 'admin_posts/post_details.html', {
                'post': book,
                'review': review_count,
                'reviews': reviews
            })
        except AdminPost.DoesNotExist:
            messages.error(request, 'No such book')
        return redirect('profile')
