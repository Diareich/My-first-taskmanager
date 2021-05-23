from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('about-me', views.about, name="about"),
	path('create-task', views.create, name='create'),
]