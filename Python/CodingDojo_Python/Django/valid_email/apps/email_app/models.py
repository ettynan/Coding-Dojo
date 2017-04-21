from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

# Create your models here.
class EmailManager(models.Manager):
    def validate_email(self, postData):
        print "in models manager", postData
        errors = [] #empty list evaluates to false

        if not EMAIL_REGEX.match(postData): #checks to see if anything entered into the email form
            errors.append("Invalid email")

        # if len(postData) < 1: #redundant, but a good check for length of email aka not blank
        #     errors.append('Email may not be blank')
        #     #return(False, errors)

        if errors: #if length of errors>0
            return (False, errors)

        else:#act of saving in the database
            new_obj = Email.objects.create(email=postData)
            return (True, new_obj)

class Email(models.Model):
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = EmailManager()

    def __unicode__(self):
        return self.email