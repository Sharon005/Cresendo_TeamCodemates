from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.home, name="home"),
	path('add/', views.add, name="add"),
	path('forms/', views.forms, name="forms"),
	path('summary/', views.summary, name="summary"),
	
]
