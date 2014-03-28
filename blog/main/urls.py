from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
    
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^(?P<pk>\d+)/$', views.PostDetailsView.as_view(), name="postDetails"),
)
