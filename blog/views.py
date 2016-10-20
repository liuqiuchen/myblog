from django.shortcuts import render
from blog.models import Blog
import datetime

# Create your views here.
def get_blogs(request):

	ctx = {
		'blogs': Blog.objects.all().order_by('-created')
	}
	return render(request, 'blog-list.html', ctx)