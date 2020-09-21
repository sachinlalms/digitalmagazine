from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Post
from django.views import generic
# Create your views here.

class Postlist(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'magazine/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'magazine/post_details.html'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','image','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False





def about(request):
    return render(request,'magazine/about.html')