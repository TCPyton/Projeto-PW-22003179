from . import views
from django.urls import path


app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view),
    path('home', views.home_page_view, name= 'home'),
    path('blog', views.blog_page_view, name = 'blog'),
    path('newBlog', views.new_blog_post, name = 'newBlog'),
    path('editBlog/<int:blog_id>', views.edit_blog_post, name = 'editBlog'),
    path('deleteBlog/<int:blog_id>', views.delete_blog_post, name = 'deleteBlog'),
    path('web', views.quizz, name = 'web'),
    path('login', views.view_login, name='login'),
    path('logout', views.view_logout, name='logout'),

]
