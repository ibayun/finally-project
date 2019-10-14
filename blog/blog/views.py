from django.http import  HttpResponse
from django.shortcuts import redirect


def redirect_url(request):
    return redirect('post_trends_url', permanent=True)
