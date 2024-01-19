from django.urls import path
from .views import *
 
urlpatterns=[

        path('getdata/',GetStudent.as_view(),name='getdata'),
        path('booksdetails/',BooksDetails.as_view(),name='booksdetails')
]
