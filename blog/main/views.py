from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from main.models import BlogPost

class IndexView(generic.ListView):
    template_name = "main/index.html"
    context_object_name = "all_posts"
    
    def get_queryset(self):
        return BlogPost.objects.order_by("blog_TimeDate")
    
class PostDetailsView(generic.DetailView):
    model = BlogPost
    template_name = "main/post.html"
    