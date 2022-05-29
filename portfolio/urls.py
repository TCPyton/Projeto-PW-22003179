from . import views
from django.urls import path


app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view),
    path('home', views.home_page_view, name= 'home'),
    path('apresentacao', views.apresentacao_view, name= 'apresentacao'),
    path('formacao', views.formacao_view, name= 'formacao'),
    path('projetos', views.projetos_view, name= 'projetos'),
    path('competencias', views.competencias_view, name= 'competencias'),
    path('newBlog', views.new_blog_post, name = 'newBlog'),
    path('editBlog/<int:blog_id>', views.edit_blog_post, name = 'editBlog'),
    path('deleteBlog/<int:blog_id>', views.delete_blog_post, name = 'deleteBlog'),
    path('blog', views.blog_page_view, name = 'blog'),
    path('quizz', views.quizz, name = 'quizz')

]
