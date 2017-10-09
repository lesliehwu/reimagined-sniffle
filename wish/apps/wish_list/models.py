# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
from django.contrib import messages

# Create your models here.

class UserManager(models.Manager):
    def reg_validate(self, post_data):
        errors = {}

        if len(post_data['name']) < 3:
            errors['name']='Name must be at least 3 characters long'
        elif not post_data['name'].isalpha():
            errors['name'] = 'Name can only contain letters'

        if len(post_data['username']) < 3:
            errors['username'] = 'Username must be at least 3 characters long'

        if len(post_data['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'

        if not post_data['confirm'] == post_data['password']:
            errors['confirm'] = 'Password fields must match'

        return errors

    def log_validate(self, post_data):
        errors = {}

        if len(self.filter(username = post_data['username'])):
            user = self.filter(username=post_data['username'])[0]
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                errors['password'] = 'Password is incorrect'
        else:
            errors['username'] = 'User not found'
        if len(post_data['username']) < 3:
            errors['username'] = 'Username must be at least 3 characters'

        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    hired = models.DateTimeField()
    objects = UserManager()

class WishManager(models.Manager):
    def validate(self, post_data):
        errors = {}
        if len(post_data['name']) < 3:
            errors['name'] = 'Field cannot be empty/must be more than 3 charcaters'
        return errors

class Wish(models.Model):
    name = models.CharField(max_length=255)
    wisher = models.ForeignKey(User, related_name = 'added_wishes')
    wishers = models.ManyToManyField(User, related_name='wishes')
    date_added = models.DateTimeField(auto_now_add = True)
    objects = WishManager()
