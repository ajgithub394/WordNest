from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),  #Empty string because it's home page
    path("post/<int:pk>",views.post_details,name='post-detail'),
    path("post/new/",views.PostCreateView.as_view(),name='post-create'), #The name will be the name of the HTML file that this view is linked to
    path("post/<int:pk>/edit/",views.PostUpdateView.as_view(),name='post-update'),
    path("post/<int:pk>/delete/",views.PostDeleteView.as_view(),name='post-delete'),
]
