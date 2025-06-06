from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from admin_posts.models import AdminPost
from .models import BuyBook, BorrowedBook, Review
from auth_user.models import UserAccount
from django.contrib.auth.mixins import LoginRequiredMixin
from tranactions.constants import RETURN_BOOK
from datetime import timezone
from .forms import UserReviewForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def email_send_messages(user, borrow_price, subject, book_name, template):
    message = render_to_string(template, {
        'user': user,
        'borrow_price': borrow_price,
        'book_name': book_name,
    })
    to_email = user.email
    send_email = EmailMultiAlternatives(subject, ' ', to=[to_email])
    send_email.attach_alternative(message, 'text/html')
    send_email.send()



class BorrowBookView(View):
    template_name = 'auth_user/profile.html'

    def get(self, request, book_id):
        books = AdminPost.objects.filter(id=book_id)
        user = request.user
        if books.exists():
            borrowed_book = AdminPost.objects.get(id=book_id)
            if borrowed_book.quantity > 0 and borrowed_book.borrow_price <= user.account.balance:
                borrowed_book.quantity -= 1
                borrowed_book.save()
                buy = BorrowedBook.objects.create(book=borrowed_book, user=user)
                buy.quantity += 1
                buy.save()
                user.account.balance -= borrowed_book.borrow_price
                user.account.save()
                messages.success(request, 'Book buy successfully')
                email_send_messages(self.request.user, borrowed_book.borrow_price, 'Book buy successfully', borrowed_book.book_name, 'books/buy_book_email.html')
            else:
                messages.error(request, 'This book is not available now !')
        return redirect('profile')

class ReturnBookView(View):
    template_name = 'auth_user/profile.html'

    def get(self, request, book_id):
        borrowed_book = get_object_or_404(BorrowedBook, id=book_id)
        user = request.user

        if not borrowed_book.returend:
            borrowed_book.returend = True
            borrowed_book.save()
            borrowed_book.quantity += 1
            borrowed_book.save()

            user.account.balance += borrowed_book.book.borrow_price
            user.account.save()

            messages.success(request, 'Book Returned Successfully!')
        else:
            messages.error(request, 'This book has already been returned!')

        return redirect('profile')
    

class CreateReviewView(View):
    template_name = 'admin_posts/review.html'

    def get(self, request, book_id):
        form = UserReviewForm()
        book = AdminPost.objects.get(id=book_id)
        reviews = Review.objects.filter(book=book)
        return render(request, self.template_name, {'form': form, 'book': book, 'reviews': reviews})

    def post(self, request, book_id):
        book = AdminPost.objects.get(id=book_id)
        user = request.user
        borrowed_book = BorrowedBook.objects.filter(user=user, book=book).order_by('-id')
        if borrowed_book.exists():
            rating = request.POST.get('rating')
            comment = request.POST.get('comment')
            Review.objects.create(user=user, book=book, rating=rating, comment=comment)
            messages.success(request, 'Review submitted successfully')
        else:
            messages.info(request, 'No book buying !')
        return redirect('details', id=book_id)






