from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
    path('profile/<slug:username>/', views.profile, name='profile'),
    path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('accounts/profile/', views.index, name='go_to_main_after_login'),
    path('create/', views.post_create, name='post_create'),

]
