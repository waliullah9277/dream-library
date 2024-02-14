from django.urls import path,include
# from .views import PostDetailsView
from .views import post_details

urlpatterns = [
    path('post-details/<int:id>/', post_details, name = 'details'),

]
