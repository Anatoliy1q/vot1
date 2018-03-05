from django.conf.urls import url
from . import views

urlpatterns = [
    url('^register/$', views.RegisterFormView.as_view()),
    url('^login/$', views.LoginFormView.as_view()),
    ]