from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView,DetailView
from blog.models import Post

urlpatterns = patterns('',
	url(r'^$', include('blog.urls')),
    url(r'^(?P<pk>\d+)$',DetailView.as_view(model=Post,template_name="post.html")),
	url(r'^about/', include('about.urls')),
	url(r'^(?i)payment/', include('payment.urls', namespace='payment')),
	url(r'^admin/', include(admin.site.urls)),
)
