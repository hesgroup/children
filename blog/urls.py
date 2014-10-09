from django.conf.urls import patterns, include, url
from django.views.generic import ListView,DetailView
from blog.models import Post

urlpatterns = patterns('',
    url(r'^$',ListView.as_view(queryset = Post.objects.all().order_by("-date")[:5],template_name="blog.html")),
)
