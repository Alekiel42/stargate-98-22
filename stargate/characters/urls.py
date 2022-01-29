from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage-page"),
    path('personnages/', views.characters, name="characters-list-page"),
    path('personnages/<slug:slug>', views.characters_details, name="characters-details-page")
]