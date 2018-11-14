from django.shortcuts import render, HttpResponse, redirect

def index(request):

	return render(request, 'books/index.html')