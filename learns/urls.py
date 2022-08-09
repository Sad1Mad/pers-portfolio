from django.urls import path
from . import views



urlpatterns = [
    path('', views.all_learns, name="all_learns"),
    path('learn', views.open_learn, name="post_learn"),
]