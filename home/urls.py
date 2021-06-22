from django.contrib import admin
from django.urls import path
from home import views
urlpatterns=[
    path("", views.index, name='home'),
    path("main",views.index , name="main"),
    path("images",views.images , name="images"),
    path("about",views.about,name="about"),
    path("services",views.services,name="services"),
    path("vision",views.vision,name="vision"),
    path("contact",views.contact,name="contact"),
    path("starter",views.starter,name="starter"),
    path("roti",views.roti, name="roti"),
    path("maincourse",views.maincourse, name="maincoure"),
    path("booking",views.booking,name="booking"),
    path("food",views.food,name="food"),
]