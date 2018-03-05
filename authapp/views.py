 #-*- coding: utf-8 -*-
 
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.contrib.auth import login

class RegisterFormView(FormView):
    form_class = UserCreationForm
    
    success_url = "/login/"
    
    template_name = "auth/register.html"
    
    def form_valid(self, form):
        #Создаем пользователся, если данные введены корректно
        form.save()
        
        #Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form) 
        
class LoginFormView(FormView):
    form_class = AuthenticationForm
    
    template_name = "auth/login.html"
    
    success_url = "/"
    
    def form_valid(self, form):
        self.user = form.get_user()
    
        login(self.request, self.user)
    
        return super(LoginFormView, self). form_valid(form)
    