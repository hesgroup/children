from blog.models import Post
from django.shortcuts import render_to_response
from django.template import RequestContext

def cats(request, pk):
	recent_post = Post.objects.all().order_by("-date")[:3]
	return render_to_response('post.html',{'recent_post':recent_post},context_instance=RequestContext(request))
# Create your views here.
