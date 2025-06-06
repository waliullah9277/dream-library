from django.urls import path
from .views import BorrowBookView, ReturnBookView,CreateReviewView

urlpatterns = [
    # other patterns
    path('buy_book/<int:book_id>/', BorrowBookView.as_view(), name='buy_book'),
    path('book-return/<int:book_id>/', ReturnBookView.as_view(), name = 'return_book'),
    path('add-review/<int:book_id>/', CreateReviewView.as_view(), name = 'add_review'),
]