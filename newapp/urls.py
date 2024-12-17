from django.urls import path
from . import views

urlpatterns=[
    path("",views.homepage),
    path("homepage",views.homepage),
    path("aboutpage",views.aboutpage),
    path("contactpage",views.contactpage),
    path("projectpage",views.projectpage),
]