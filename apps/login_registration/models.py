# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9+-_.]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def registration_validation(self, post_data):
        errors = []
        if len(post_data["name"]) < 1:
            errors.append("Name is required")
        elif len(post_data["name"]) < 2:
            errors.append("Name must be at least 2 characters long")

        # if len(post_data["last"]) < 1:
        #     errors.append("Last name is required")
        # elif len(post_data["last"]) < 2:
        #     errors.append("Last name must be at least 2 characters long")

        if len(post_data["email"]) < 1:
            errors.append("Email is required")
        elif not EMAIL_REGEX.match(post_data["email"]):
            errors.append("Invalid email")
        else:
            list_of_users_matching_email = User.objects.filter(email=post_data["email"].lower())
            if len(list_of_users_matching_email) > 0:
                errors.append("Email already exists")

        if len(post_data["password"]) < 1:
            errors.append("Password is required")
        elif len(post_data["password"]) < 8:
            errors.append("Password must be 8 characters or more")

        if len(post_data["confirm"]) < 1:
            errors.append("Confirm password is required")
        elif post_data["password"] != post_data["confirm"]:
            errors.append("Confirm password must match Password")

        if len(errors) > 0:
            return (False, errors)
        else:
            user = User.objects.create(
                name=post_data["name"],
                email=post_data["email"].lower(),
                password=bcrypt.hashpw(post_data["password"].encode(), bcrypt.gensalt())
            )
            return (True, user)

    def login_validation (self,post_data):
        errors = []
        if len(post_data["email"]) < 1:
            errors.append("Email is required")
        elif not EMAIL_REGEX.match(post_data["email"]):
            errors.append("Invalid email")
        else:
            list_of_users_matching_email = User.objects.filter(email=post_data["email"].lower())
            if len(list_of_users_matching_email) < 1:
                errors.append("Email does not exist")

        if len(post_data["password"]) < 1:
            errors.append("Password is required")
        elif len(post_data["password"]) < 8:
            errors.append("Password must be 8 characters or more")

        if len(errors) <1:
            user = list_of_users_matching_email[0] #contains all the data about the specific user
            hash1 = user.password
            if bcrypt.checkpw(post_data["password"].encode(), hash1.encode()):
                return (True, user)                                             #check if it works
            else:
                errors.append("Password is incorrect")

        if len(errors) >0:
            return (False, errors)

class User(models.Model):
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
# Create your models here.
