from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm, PostForm, ProfileForm, CategoryForm, RatingForm, BannersProfileForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
import re
from account.decorators import check_user_able_to_see_page
from .models import Profile, Rating, BannersProfile
from post.models import Post, Category
from django.shortcuts import redirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg, Count
from django.contrib.auth.decorators import user_passes_test


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    print('Autenticação bem sucedida')
                    return render(request, 'post/home.html')
                else:
                    print('Conta desabilitada')
                    return HttpResponse('Conta desabilitada')
            else:
                print(' Login inválido ')
                return HttpResponse('Login inválido')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})





@login_required
def dashboard(request):   
    return render(request, 'account/dashboard.html')



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            try:
                new_user = user_form.save(commit=False)
                new_user.set_password(user_form.cleaned_data['password'])
                new_user.save()
                return render(request, 'account/register_done.html', {'new_user': new_user})
            except Exception as e:
                messages.error(request, f'Erro ao registrar usuário: {e}')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})





@login_required
@check_user_able_to_see_page("NOCTURNA ARCANA")
def create_profile(request):      
    if Profile.objects.filter(user=request.user).exists():        
        return redirect(reverse('edit_profile'))   
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)
        banners_form = BannersProfileForm(request.POST, request.FILES)

        if profile_form.is_valid() and banners_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            
        banners = request.FILES.getlist('banners')
        if banners < 5:
            for banner in banners:
                    BannersProfile.objects.create(profile=profile, banners=banner)            
            return redirect(reverse('dashboard'))
        else:
            profile_form = ProfileForm()
            banners_form = BannersProfileForm()  
    else:
        profile_form = ProfileForm()
        banners_form = BannersProfileForm()  
    return render(request, 'account/create_profile.html', {'profile_form': profile_form,"banners_form":banners_form })


@login_required
@check_user_able_to_see_page("NOCTURNA ARCANA")
def edit_profile(request):
    if not Profile.objects.filter(user=request.user).exists():       
        return redirect(reverse('create_profile')) 
    profile = Profile.objects.get(user=request.user)
    banners = BannersProfile.objects.filter(profile=profile)
    
    if request.method == 'POST':
        profile_form = ProfileForm(instance=profile, data=request.POST, files=request.FILES) 
        banners_form = BannersProfileForm(data=request.POST, files=request.FILES)
   
        if profile_form.is_valid() and banners_form.is_valid():
            profile_form.save()   
            BannersProfile.objects.filter(profile=profile).delete()        
            banners_list = request.FILES.getlist('banners')
            for banner in banners_list:
                BannersProfile.objects.create(profile=profile, banners=banner)  
            return redirect(reverse('dashboard'))    
                
    else:
        profile_form = ProfileForm(instance=profile)
        banners_form = BannersProfileForm()    
    return render(request, 'account/edit_profile.html', {'profile_form': profile_form, 'banners_form':banners_form, 'banners':banners})

def profile_prices(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    banners = BannersProfile.objects.filter(profile=profile)
    return render(request, 'account/profile_prices.html', {'profile': profile, 'banners':banners})

def list_profile(request):
    profiles = Profile.objects.all()
    return render(request, 'account/consult.html', {'profiles':profiles}) 



def is_authenticated(user):
    return user.is_authenticated


def profile_detail(request, slug):
    exists = None
    profile = get_object_or_404(Profile, slug=slug)
    ratinggs = profile.ratings.filter().order_by("-rating", "-created")     
    new_rating = None
    form = RatingForm()
    if request.method == 'POST':
        form = RatingForm(data=request.POST)
        if form.is_valid():
            if is_authenticated(request.user):                
                existing_rating = Rating.objects.filter(profile=profile, user=request.user).exists()
                if not existing_rating:                  
                    new_rating = form.save(commit=False)
                    new_rating.profile = profile            
                    new_rating.user = request.user             
                    new_rating.save()        
                    avg_rating = Rating.objects.filter(profile=profile).aggregate(Avg('rating'))['rating__avg']
                    total_rating = Rating.objects.filter(profile=profile).count()  
                    Profile.objects.filter(id=profile.id).update(average_rating=avg_rating, total_rating=total_rating)           
                    return redirect('profile_detail', slug=profile.slug)
                else:                   
                    return redirect('/')
            else:                
                return redirect('login')
    existing = Rating.objects.filter(profile=profile, user=request.user).exists()
    if existing:
        exists = True
    else:
        exists = False     
    return render(request, 'account/profile_detail.html', {'profile': profile, 'form': form, 'new_rating': new_rating, 'ratinggs':ratinggs, 'exists':exists})


@login_required
def update_rating(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    rating = get_object_or_404(Rating, profile=profile, user=request.user) 
    try:
        if request.method == 'POST':
            form = RatingForm(instance=rating, data=request.POST)
            if form.is_valid():
                form.save()
                avg_rating = Rating.objects.filter(profile=profile).aggregate(Avg('rating'))['rating__avg']
                total_rating = Rating.objects.filter(profile=profile).count()  
                Profile.objects.filter(id=profile.id).update(average_rating=avg_rating, total_rating=total_rating)
                return redirect('profile_detail', slug=profile.slug)
        else:
            form = RatingForm(instance=rating)  
    except:
        return redirect('profile_detail', slug=profile.slug)
    return render(request, 'account/profile_detail.html', {'profile': profile, 'form': form, 'rating': rating})


@login_required
@check_user_able_to_see_page("NOCTURNA ARCANA")
def create_category(request):
    if request.method == 'POST': 
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, 'Categoria criada com sucesso')
            return redirect(reverse('create_post')) 
        
    else:
        form = CategoryForm()    
    return render(request, 'account/edit_post.html', {'form': form})


@login_required
@check_user_able_to_see_page("NOCTURNA ARCANA")
def create_post(request):    
    if request.method == 'POST':        
        form = PostForm(request.POST, request.FILES)        
        if form.is_valid():            
            post = form.save(commit=False)
            post.user_post = request.user
            post.save()
            messages.success(request, 'Postagem criada com sucesso')
            return redirect(reverse('dashboard')) 
        else:            
            messages.error(request, 'Erro ao criar postagem')
            
    else:
        form = PostForm()    
    return render(request, 'account/create_post.html', {'form': form, 'categorys': Category.objects.all()})


@login_required
@check_user_able_to_see_page("NOCTURNA ARCANA")
def edit_post(request, year, month, day, id, post):    
    post_obj = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post, created__year=year, created__month=month, id=id, created__day=day)
    
    if request.method == 'POST':
        form = PostForm(instance=post_obj, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Artigo atualizado com sucesso')
            return redirect(reverse('dashboard'))
        else:            
            print(form.errors)
            messages.error(request, 'Erro ao atualizar o Artigo')
    else:
        form = PostForm(instance=post_obj)  
    
    return render(request, 'account/edit_post.html', {'form': form, 'post': post_obj, 'categorys': Category.objects.all(), 'form_errors': form.errors})



@login_required
@check_user_able_to_see_page("NOCTURNA ARCANA")
def delete_post(request, year, month, day, id, post):    
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post, created__year=year, created__month=month, created__day=day, id=id)
    try:   
        post.delete()
        messages.success(request, 'Artigo exluído com sucesso')
        return redirect(reverse('my_posts'))
    except ObjectDoesNotExist:
        messages.error(request, 'Artigo não encontrado!')
    except Exception as e:
        messages.error(request, 'Ocorreu um erro ao excluir o Artigo')
    return render(request, 'account/my_posts.html', {'post': post})


@login_required
@check_user_able_to_see_page("NOCTURNA ARCANA")
def my_posts(request):    
    posts = Post.objects.filter(user_post=request.user)
    return render(request, 'account/my_posts.html', {'posts': posts})