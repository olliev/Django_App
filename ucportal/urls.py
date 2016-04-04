from django.conf import settings
from django.conf.urls import include, url
from . import views
app_name = 'ucportal'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^exam/$', views.exam, name = 'exam'),
]