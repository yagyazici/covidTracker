from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("europe/",views.europe,name="europe"),
    path("asia/", views.asia, name="asia"),
    path("africa/", views.africa, name="africa"),
    path("australia-ocenia/",views.australia_oceania,name="australia-oceania"),
    path("north-america/", views.north_america, name="north-america"),
    path("south-america/", views.south_america, name="south-america"),
]
