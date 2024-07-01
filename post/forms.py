from django import forms
from ckeditor.fields import RichTextFormField
from .models import Post, Comment, Response

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body_post', 'category', 'image']  # Adicione 'slug' aos campos
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'body_post': RichTextFormField(config_name='default'),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoria'}),
            'image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imagem'}),
        }


class Searchform(forms.Form):
    query = forms.CharField()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body_comment']

        
class CommentEditForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body_comment']

        
class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['body_response']