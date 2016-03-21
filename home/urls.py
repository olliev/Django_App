from django.conf.urls import include, url

from . import views
app_name = 'home'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^t/$', views.current_datetime),
	#URLconf for demo 
	url(r'^d/$', views.demo, name='demo'),
	url(r'^search/$', views.search, name = "search"),
	url(r'^contact/$', views.contact)
]
