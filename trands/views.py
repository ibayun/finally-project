from django.shortcuts import render


def index(request):
    return render(request, 'trands/trandsPage.html')
