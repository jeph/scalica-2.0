from django.conf.urls import include, url

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^stream/(?P<user_id>[0-9]+)/$', views.stream, name='stream'),
    url(r'^post/$', views.post, name='post'),
    url(r'^follow/$', views.follow, name='follow'),
    url(r'^register/$', views.register, name='register'),
    url(r'^upload/$', views.upload, name='register'),
    url(r'^tag/(?P<photo_id>[0-9A-Za-z\-]+)/$', views.tag, name='tag'),
    url('^', include('django.contrib.auth.urls'))
]
