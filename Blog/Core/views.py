from django.shortcuts import render, redirect, reverse
from django.views.generic import (
    CreateView, UpdateView, DeleteView, DetailView, ListView, 
    )
from .models import Post
from .forms import PostCreationForm
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


class PostListView(ListView):
    model = Post
    template_name = "Core/post_list.html"
    context_object_name = "posts"
    paginate_by = 3

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = "Core/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        is_author = False
        if self.object.author == self.request.user:
            is_author = True
        context['is_author'] = is_author
        return context

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = "Core/post_create.html"
    form_class = PostCreationForm
    
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        form.save()
        return redirect(reverse('Core:post-detail', kwargs={'slug': form.instance.slug}))

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = "Core/post_create.html"
    form_class = PostCreationForm

    def form_valid(self,form):
        form.instance.author = self.request.user
        form.save()
        return redirect(reverse('Core:post-detail', kwargs={'slug': form.instance.slug}))
    
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(author=self.request.user)
        return qs


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = "Core/post_delete.html"
    success_url = reverse_lazy('Core:post-list')

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(author=self.request.user)
        return qs

class SearchResultsView(ListView):
    model = Post
    template_name = "Core/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        search_query = self.request.GET.get('q')
        queryset = Post.objects.filter(Q(title__icontains=search_query))
        return queryset