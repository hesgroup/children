from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post
from payment.views import StartView

urlpatterns = patterns('',
                       url(r'^(?i)start$', StartView.as_view(),name='start'),
)
