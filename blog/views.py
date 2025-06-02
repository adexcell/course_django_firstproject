from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest


def index(request: WSGIRequest) -> HttpResponse:
    return render(request, 'blog/index.html', context={'site': 'mysite.com'})


def contact(request):
    return redirect('blog:about')
