from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.latest_book, name="latest_book"),
    url(r'^book/(?P<pk>\d+)/$', views.book_detail, name='book_detail'),
]