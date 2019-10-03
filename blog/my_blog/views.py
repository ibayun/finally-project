from django.shortcuts import render


# Create your views here.

def posts_message_test(request):
    return render(request, 'network/index.html')

