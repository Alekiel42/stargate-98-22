from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'characters/index.html')


def characters(request):
    return render(request, 'characters/characters-list.html')


def characters_details(request, slug):
    return render(request, 'characters/character-details.html')
