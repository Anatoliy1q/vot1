from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.latest_book, name="latest_book"),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^book/new/$', views.book_new, name='book_new'),
    url(r'^book/(?P<pk>\d+)/$', views.book_detail, name='book_detail'),
]