from django.urls import path
from django.urls import path
from store import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.home, name="home"),
	path('add/', views.add, name="add"),
	path('forms/', views.forms, name="forms"),
	
]
