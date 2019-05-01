from django.urls import path
from . import views
from .views import AirlineListView
urlpatterns = [
    #path('', views.home, name='home-page'),
    path('', AirlineListView.as_view(), name='home-page'),
]
