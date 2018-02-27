# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages

def index (request):
    return render(request, "login_registration/index.html")

def registration (request):
    data_from_registration = User.objects.registration_validation(request.POST)
    if data_from_registration[0]:
        request.session["user_id"] = data_from_registration[1].id
        messages.add_message(request, messages.SUCCESS, "You successfully registered!")
        return redirect("/loggedin")
    else:
        for error in data_from_registration[1]:
            messages.add_message(request, messages.ERROR, error)
        return redirect("/")

def login (request):
    data_from_login = User.objects.login_validation(request.POST)
    if data_from_login[0]:
        request.session["user_id"] = data_from_login[1].id
        messages.add_message(request, messages.SUCCESS, "You successfully logged in!")
        return redirect("/loggedin")
    else:
        for error in data_from_login[1]:
            messages.add_message(request, messages.ERROR, error)
        return redirect("/")

def loggedin(request):
    return redirect("/travels")

# Create your views here.
