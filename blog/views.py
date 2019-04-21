from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . models import Blog

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

class BlogsListView( ListView ) :
	model = Blog
	template_name = "blog/home.html"
	context_object_name = 'blogs'
	ordering = ['-date_posted']

class BlogsDetailView( DetailView ) :
	model = Blog

class BlogsCreateView( LoginRequiredMixin, CreateView ) :
	model = Blog
	fields = ['title', 'content']

	def form_valid( self, form ) :
		form.instance.author = self.request.user
		return super().form_valid( form )

class BlogsUpdateView( LoginRequiredMixin, UserPassesTestMixin, UpdateView ) :
	model = Blog
	fields = [ 'title', 'content' ]

	def form_valid( self, form ) :
		form.instance.author = self.request.user
		return super().form_valid( form )

	def test_func( self ):
		post = self.get_object()
		if self.request.user == post.author :
			return True
		return False

class BlogsDeleteView( DeleteView ) :

	model = Blog

	success_url = "/"

	def test_func( self ):
		post = self.get.object()
		if self.request.user == post.author :
			return True
		return False