# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.contrib import auth
from index import models as index_models
from index.email_module import sendEmail
from django.views.decorators.csrf import csrf_exempt

def about(request):
	argv = {}
	argv['commands'] = index_models.UserProfile.objects.all()
	argv['commands_len'] = len(index_models.UserProfile.objects.all())
	return render(
	 	request, 'about.html', argv
	 	)

def index(request):
	argv = {}
	argv['commands_len'] = len(index_models.UserProfile.objects.all())

	return render(request, 'index.html', argv)

@csrf_exempt
def add_to_db(request):
	if request.method == "POST":
		a = index_models.add_to_db.objects.create(add_to_db_text=request.POST['message'])
		a.save()
	argv = {}
	argv['mes'] =index_models.add_to_db.objects.all()
	return render(request, 'add_to_db.html')
