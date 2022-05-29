from django import forms
from django.forms import ModelForm
from .models import Blog, Quizz


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

        widgets = {

            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'O seu nome completo: '}),
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Insira aqui o title do seu novo post.'}),
            'description' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Faça uma breve descrição do seu post.'}),
            'link' : forms.URLInput(attrs={'class' : 'form-control', 'placeholder' : 'www.google.com'})
            

        }

        labels = {
            'author' : 'Autor',
            'title' : 'Título',
            'data' : 'Data',
            'description' : 'Descrição',
            'image' : 'Imagem',



        }

        help_texts = {
            'data' : 'Meta a data na ordem : YYYY/MM/DD'
        }


class QuizzForm(ModelForm):
    class Meta:
        model = Quizz
        fields = '__all__'

        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'O seu nome completo: '}),
        }

        labels = {
            'question1' : 'O que significa HTML?',
            'question2' : 'CSS significa Cascading Style Sinal',
            'question3' : 'Django é uma framework para desenvolvimento rápido para web',
            'question4' : 'Em que ano foi lançado a framework Django?',
            'question5' : 'A ultima versão disponível de HTML até agora é o HTML5'
        }