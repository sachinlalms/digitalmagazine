from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Post
from django.views import generic
# Create your views here.

class Postlist(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'magazine/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'magazine/post_details.html'


 





def about(request):
    return render(request,'magazine/about.html')