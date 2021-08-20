from django.urls import path
from .views import *


urlpatterns = [
    path('', home_page, name="home-page"),
    path('about/', about_me, name="about-me"),
    path('project/', project_view, name="project-view"),
    path('contact/', contact_me, name="contact-me")
]
