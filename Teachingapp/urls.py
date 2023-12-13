from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.landing_page, name = "home"),
    #path to Add event
    path('add_event', views.add_event, name="add_event"),
    #path to view event data individually
    path('event/<str:event_id>', views.event, name="event"),
    #path to edit event
    path('edit_event', views.edit_event, name="edit_event"),
    #path to delete event
    path('delete_event/<str:event_id>', views.delete_event, name="delete_event"),
    #path to detail event
    path('detail/<str:event_id>', views.Event_details, name="detail"),
    path("event-list", views.event_listajax, name="event-list"),
    path("searchevents", views.searchevents, name="searchevents"),
]   




