# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *
import bcrypt
from django.db import connection, transaction
from django.contrib import messages

# Create your views here.

def index(request):
    if 'id' not in request.session:
        request.session['id'] = -1
    return render(request, 'index.html')

def register(request):
    errors = User.objects.reg_validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            messages.error(request, message, extra_tags = field)
        return redirect('/')
    else:
        hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(name = request.POST['name'], username = request.POST['username'], password = hash1, hired = request.POST['date'])
        request.session['id'] = user.id
        return redirect('/dashboard')

def login(request):
    errors = User.objects.log_validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            messages.error(request, message, extra_tags =field)
        return redirect('/')
    else:
        user = User.objects.get(username = request.POST['username'])
        request.session['id'] = user.id
        return redirect('/dashboard')

def dashboard(request):
    context = {
            "user":User.objects.get(id=request.session['id']),
            "wishes":Wish.objects.all(),
            "my_wishes":Wish.objects.filter(wishers = request.session['id'])
    }
    return render(request, 'dashboard.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def add(request):
    context = {
            "user":User.objects.get(id=request.session['id'])
    }
    return render(request, 'add.html', context)

def remove(request, item_num):
    item = Wish.objects.get(id=item_num)
    wisher = User.objects.get(id=request.session['id'])
    wisher.wishes.remove(item)
    return redirect('/dashboard')

def delete(request, item_num):
    item = Wish.objects.filter(id=item_num)
    item.delete()
    return redirect('/dashboard')

def add_to(request,item_num):
    item = Wish.objects.get(id=item_num)
    wisher = User.objects.get(id=request.session['id'])
    wisher.wishes.add(item)
    return redirect('/dashboard')

def create(request):
    errors = Wish.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            messages.error(request, message, extra_tags = field)
        return redirect('/add')
    else:
        item = Wish.objects.create(name = request.POST['name'], wisher=User.objects.get(id=request.session['id']))
        return redirect('/dashboard')

def show(request, item_num):
    context = {
            "wish":Wish.objects.get(id = item_num),
            "wishers":User.objects.filter(wishes=item_num)
    }
    return render(request, 'show.html',context)
