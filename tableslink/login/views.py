# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import RegistrationForm

# Create your views here.

def user_registration(request):
    """
    Handles user registration
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                    email=form.cleaned_data['email'],
                    )
            return HttpReponseRedirect('/users/success/')
    else:
        form = RegistrationForm() 
        return render(request, 'register.html', {'form': form})

def user_login():
    pass

def user_logout():
    pass
