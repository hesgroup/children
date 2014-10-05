from django.conf.urls import patterns, include, url
from django.views.generic import ListView,DetailView
from about.models import About

urlpatterns = patterns('',
    url(r'^$',ListView.as_view(queryset = About.objects.all(),template_name="about.html")),
)
