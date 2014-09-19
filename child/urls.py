from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^(?i)blog/', include('blog.urls')),
                       url(r'^(?i)payment/', include('payment.urls', namespace='payment')),
                       url(r'^admin/', include(admin.site.urls)),
)
