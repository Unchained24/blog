
from django.urls import path
from .import views

urlpatterns = [
    path('',views.post_list, name= "post_list"),
    # urls('',views.post_list, name= "post_list"),
    path('post_details/<int:pk>/',views.post_details, name= "post_details"),
    path('post_new/', views.post_new, name="post_new"),
    path('post_edit/<int:pk>', views.post_edit, name="post_edit"),
]