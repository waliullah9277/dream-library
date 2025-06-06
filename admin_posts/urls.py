from django.urls import path,include
# from .views import PostDetailsView
from .views import post_details

urlpatterns = [
    path('post-details/<int:id>/', post_details, name = 'details'),
    # path('post/<int:id>/', post_details, name='post_details'),


]
