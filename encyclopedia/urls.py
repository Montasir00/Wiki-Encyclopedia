from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),                           # Homepage showing all entries
    path("search/", views.search_results, name="search_results"),  # Search functionality
    path("wiki/<str:TITLE>/", views.entry_page, name="entry_page"),  # Individual entry page
    path("create/", views.create_page, name="create_page"),        # Create a new entry page
    path("random/", views.random_page, name="random_page"),        # Random entry page
]
