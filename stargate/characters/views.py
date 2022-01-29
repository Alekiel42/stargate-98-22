from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'characters/index.html')


def characters(request):
    pass


def characters_details(request):
    pass
