from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView, SearchResultsView

app_name = 'Core'

urlpatterns = [
    path('', PostListView.as_view(), name="post-list"),
    path('posts/create/', PostCreateView.as_view(), name="post-create"),
    path('posts/<str:slug>/', PostDetailView.as_view(), name="post-detail"),
    path('posts/<str:slug>/edit/', PostUpdateView.as_view(), name="post-update"),
    path('posts/<str:slug>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('search/', SearchResultsView.as_view(), name="search-results"),
]