from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("aboutus/", views.ourvision, name="aboutus"),
    path('visit/', views.visit, name="visit"),
    path('contactus/', views.contactus, name="contactus")
]