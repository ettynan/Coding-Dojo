from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re, bcrypt
from bcrypt import hashpw

FIRST_NAME_REGEX = re.compile(r'^[a-zA-Z]*$')
LAST_NAME_REGEX = re.compile(r'^[a-zA-Z]*$')
EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]*$)")
# Create your models here.

class UserManager(models.Manager):
    def validate_user(self, data):
        print "models user email validate", data
        errors = []

        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        password = data['password']
        confirm_pw = data['confirm_pw']
        # birth_date = data['birth_date']

        # if len(birth_date) > 0:
        #     try:
        #         formatted_birth_date = datetime.strptime(data['birth_date'], '%Y-%m-%d')
        #     except:
        #         errors.append("Birth date invalid")
        #         print type(birth_date), birth_date

        if not (FIRST_NAME_REGEX.match(data['first_name']) and len(data['first_name']) > 1):
            errors.append('First name must be at least 2 characters and no numbers or special characters')

        if not (LAST_NAME_REGEX.match(data['last_name']) and len(data['last_name']) > 1):
            errors.append('Last name must be at least 2 characters and no numbers or special characters')

        if len(email) < 5:
            errors.append('Email field must be filled out')
        elif not EMAIL_REGEX.match(data['email']):
            errors.append('Invalid email')

        if User.objects.filter(email=data['email']).exists():
            errors.append('Email already in use')

        print errors
        if errors:
            return(False, errors)
        else:
            user = self.create(first_name=first_name, last_name=last_name, email = email, password = password)
            print user
            return(True, "Registered Successfully", user)

    # def login(self, data):
    #     errors = []

    #     if not EMAIL_REGEX.match(data['email']): 
    #         errors.append('Invalid email')

    #     return(True, "Logged in successfully")


class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 20)
    # birth_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()

    # def __inicode__(self):
    #     return self.first_name

