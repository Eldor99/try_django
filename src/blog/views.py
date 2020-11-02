from django.shortcuts import render

# Create your views here.
from .models import BlogPost

obj = BlogPost.objects.get(id=2)

def blog_post_detail_page(request):
	template_name = 'blog_post_detail_page.html'
	context = {'object': obj}
	return render(request, template_name,context)