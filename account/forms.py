from django import forms
from django.contrib.auth.models import User
from .models import Profile, Rating, BannersProfile
from ckeditor.fields import RichTextFormField
from ckeditor.widgets import CKEditorWidget
from post.models import Post, Category

class LoginForm(forms.Form):
    username = forms.CharField(label='Nome de usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita a senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('As senhas não coincidem.')
        return cd['password2']

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email já está em uso.')
        return data


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError('Email já está em uso.')
        return data


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'slug', 'biographia', 'instagram', 'facebook', 'tiktok', 'whatsapp', 'telegram'] 
        widgets = {            
            'biographia': forms.CharField(widget=CKEditorWidget()),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Instagram'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Facebook'}),
            'tiktok': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tik Tok'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Whatsapp'}),
            'telegram': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telegram'}),
        }
class BannersProfileForm(forms.ModelForm):
    class Meta: 
        model = BannersProfile
        fields = ['banners']
        widgets = {
            'banners': forms.ClearableFileInput(attrs={'accept': 'image/*'})  # Add this line
        }



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoria'}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body_post', 'category', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'body_post': forms.CharField(widget=CKEditorWidget()),
            'category': forms.Select(attrs={'class': 'form-control'}),  # Usamos Select para um dropdown
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Imagem'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Preencher as opções do campo 'category' com as categorias existentes
        self.fields['category'].queryset = Category.objects.all()

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['comment', 'rating']









