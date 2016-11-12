from django.conf.urls import url

#from photos.views import list_posts
#from photos.views import view_post

from . import views

app_name = 'photos'

#urlpatterns = [
#    url(r'^photos/(?P<pk>[0-9]+)/$', view_post, name='view'),
#    url(r'^photos/$', list_posts, name='list'),
#]

urlpatterns = [
    url(r'^new/$', views.create_post, name='new'),
    url(r'^(?P<pk>[0-9]+)/$', views.view_post, name='view'),
    url(r'^$', views.list_posts, name='list'),
]
