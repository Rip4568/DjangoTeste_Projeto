from django.urls import path
from . import views

app_name = 'Teste_app'

urlpatterns = [
    path('',views.HomeTemplateView.as_view(),name='homeview'),
    path('contas/register/',views.UserCreateView.as_view(),name='register'),    
    path('contas/update/<int:pk>',views.UserUpdateView.as_view(),name='update'),
    #criar caminho para a criação de novos posts
    path('criar-post',views.PostCreateView.as_view(),name='postcreate'),
    #criar o caminho para a vizualização de todos os post
    path('listar-post/',views.PostListView.as_view(),name='postlist'),
    #cirar o caminho para o detalhe dos post
    path('detalhar-post/<int:pk>',views.PostDetailView.as_view(),name='postdetail')
]