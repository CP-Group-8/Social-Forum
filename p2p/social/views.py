from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_protect ,csrf_exempt


# Create your views here.
def index(request):
	return render(request, 'index.html', {})