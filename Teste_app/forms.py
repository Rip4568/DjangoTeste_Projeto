from email.policy import default
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from Teste_app.models import Post

class RegisterUserForm(UserCreationForm):
    #name = forms.CharField(max_length=255,label='Nome',required=False)
    #email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ['username','password1','password2']



class PostForm(forms.ModelForm):
    imagem = forms.ImageField(allow_empty_file=False,error_messages={'msg1':'Obrigatorio envio de imagens'},label="Faça upload de alguma imagem aqui")
    class Meta:
        model = Post
        fields = '__all__'
