from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView,CreateView,UpdateView,ListView,DetailView
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.contrib.auth.models import User
from requests import request
from .forms import RegisterUserForm,PostForm
from .models import Post

# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = "Teste_app/index.html"
    

class UserCreateView(CreateView):
    model = User #o RegisterUserForm já possrui o model linkado para o mesmo modelo, logo não precisa
    form_class = RegisterUserForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('Teste_app:homeview')
    #como editar o modelo de usuario e fazer com que receba uma foto de perfil
    #como inserir o campo de email junto com o formulario de criação

class UserUpdateView(UpdateView):
    form_class = RegisterUserForm
    model = User
    template_name = "registration/login.html"
    #success_url = reverse_lazy('Teste_app:homeview')

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "Teste_app/criar-post.html"
    success_url = '/listar-post'
    
    
    

class PostListView(ListView):
    model = Post
    template_name = 'Teste_app/listar-post.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        self.queryset = super().get_queryset()
        if self.request.GET.get('apagar-post'):
            print(self.request.GET.get('apagar-post'))
            Post.objects.all().delete()
            self.queryset = super().get_queryset()
        
        return self.queryset




class PostDetailView(DetailView):
    model = Post
    template_name = "Teste_app/criar-post.html"
    context_object_name = 'post'

    

