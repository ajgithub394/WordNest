from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    posts = Post.objects.all() #Getting all the posts in a single variable
    return render(request, 'blog/home.html',{"posts" : posts})


#View details of a post
@login_required
def post_details(request,pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
    }
    return render(request,'blog/post_detail.html', context)

#New Post
class PostCreateView(CreateView):  #Class-based view
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title','content']
    success_url = reverse_lazy("home")  #if post creation successful redirect to home


#Update Post
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title','content']
    success_url = reverse_lazy("home")  #if post creation successful redirect to home


#Delete Post
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy("home")  #if post creation successful redirect to home