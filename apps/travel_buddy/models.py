# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from ..login_registration.models import User
from django.contrib import messages

class TripManager(models.Manager):
    def trip_validation(self,post_data):
        errors = []

        if len(post_data['destination']) < 1:
            errors.append("Destination is required")

        if len(post_data['description']) <1:
            errors.append("Description is required")

        if len(post_data['start_date']) <1:
            errors.append("Start Date is required")
        else:
            startDate = datetime.strptime(post_data["start_date"], "%Y-%m-%d")
            if startDate < datetime.now():
                errors.append("Start Date can't be in the past")

        if len(post_data['end_date']) <1:
            errors.append("End Date is required")
        else:
            endDate = datetime.strptime(post_data["end_date"], "%Y-%m-%d")
            if endDate < startDate:
                errors.append("End Date can't be before Start Date")

        if len(errors)>0:
            return (False, errors)
        else:
            trip_data = Trip.objects.create(
                destination = post_data["destination"],
                description = post_data["description"],
                start_date = post_data["start_date"],
                end_date = post_data["end_date"]
            )
            return (True,trip_data)

class Trip(models.Model):
    destination = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, related_name = "trips") # Many to many relationship
    objects = TripManager()
# Create your models here.
