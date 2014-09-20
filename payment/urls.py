from django.conf.urls import patterns, include, url
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView
from blog.models import Post
from payment.views import StartView, ResultView

urlpatterns = patterns('',
                       url(r'^(?i)start$', StartView.as_view(), name='start'),
                       url(r'^(?i)result/(?P<transaction_id>\d*)$', csrf_exempt(ResultView.as_view()), name='start'),
)
