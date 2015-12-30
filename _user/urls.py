from django.conf.urls import url
from . import views
# comment

urlpatterns = [
	url(r'^$', views.index, name='index'),
]
