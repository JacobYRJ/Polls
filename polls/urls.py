from django.conf.urls import url
from . import views

app_name = 'polls'  #命名空间
urlpatterns = [
	url(r'^$', views.index, name='index'),  #命名URL，在其他地方明确地引用它
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]