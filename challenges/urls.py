from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.index),
    path("", views.index, name="index"),  # empty path will trigger index view of the app challenge
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]
