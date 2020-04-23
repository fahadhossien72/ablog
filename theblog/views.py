from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from .models import Post
from .forms import PostForm,EditForm
from django.urls import reverse_lazy
# Create your views here.
# def home(request):
# return render(request, "home.html")


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering=['-id']


class ArticleDetailView(DetailView):

    model = Post
    template_name = 'detail.html'


class AddpostView(CreateView):
    model = Post
    form_class=PostForm
    template_name = 'post.html'
    #fields = '__all__'

class BlogEditView(UpdateView):
	model=Post
	form_class=EditForm
	template_name='edit.html'
	#fields=['title', 'title_tag', 'body']

class BlogDeleteView(DeleteView):
    model=Post
    template_name='delete.html'
    success_url= reverse_lazy ('home')


