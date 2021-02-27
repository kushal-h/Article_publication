from django.urls import path
from .views import *
urlpatterns = [
    path('post/',post_list ),
path('post/<slug:slug>',post_details ),
]
