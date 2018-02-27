# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Trip#CLasses from models here
from ..login_registration.models import User
from django.contrib import messages

def travels(request):
    data = {
    #users = models.ManyToManyField(User, related_name = "Trips") # Many to many relationship
        "user_name": User.objects.get(id = request.session["user_id"]),
        "user_trips": Trip.objects.filter(users = request.session["user_id"]),#User.objects.filter(id = request.session["user_id"]).all(),
        "users_data": Trip.objects.all()
        #"user_data" : Trip.objects.filter()
    }
    return render(request, "travel_buddy/travels.html", data)

def add(request):
    return render(request, "travel_buddy/add_trip.html")

def adding_trip(request):
    trip_data_validated = Trip.objects.trip_validation(request.POST)
    if trip_data_validated[0]:
        user = User.objects.get(id = request.session["user_id"])
        trip = Trip.objects.last()
        user.trips.add(trip)
        messages.add_message(request, messages.SUCCESS, "You added a trip")
        return redirect("/travels")
    else:
        for error in trip_data_validated[1]:
            messages.add_message(request.ERROR, error)
    return redirect("/")

def logout(request):
    del request.session["user_id"]
    request.session.modified = True
    return redirect("/")

def destination(request):
    trip_id = request.POST["trip_id"]
    data = {
        "trip" : Trip.objects.get(id = trip_id)
    }
    return render(request, "travel_buddy/destination.html", data)

def join(request):
    trip = Trip.objects.get(id = request.POST["trip_id"])
    user = User.objects.get(id = request.session["user_id"])
    user.trips.add(trip)
    messages.add_message(request, messages.SUCCESS, "Congratulations, you joined another trip")
    return redirect("/travels")
# Create your views here.
