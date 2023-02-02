from django.urls import path 
from .views import Index ,Details,NewPost,EditPost,DeletePost

urlpatterns = [ 
    path('',Index.as_view(), name = "home"), 
    path('post/<int:pk>',Details.as_view() , name = 'details'), 
    path('post/new',NewPost.as_view(), name = 'new_post'),
    path('post/<int:pk>/edit',EditPost.as_view(), name = 'edit_post'),
    path('post/<int:pk>/delete',DeletePost.as_view(), name = 'delete_post'),
]