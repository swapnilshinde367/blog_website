from django.shortcuts import render
from django.http import HttpResponse
from . models import Blog
# Create your views here.
def home( request ) :

	blogs = Blog.objects.all()
	context = { 'title' : 'Home',
				'blogs' : blogs }
	return render( request = request,
					template_name = "blog/home.html",
					context = context )

def show_blog( request, blog_id ) :
	blog = Blog.objects.get( id = blog_id )
	context = { 'title' : 'Blog - ' + blog.title,
				'blog' : blog }
	return render( request = request,
					template_name = "blog/blog.html",
					context = context )


def about( request ) :
	context = { 'title': 'About' }
	return render( request = request,
					template_name = "blog/about.html",
					context = context )

