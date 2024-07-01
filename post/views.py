from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Comment, Category, Response, Home
from .forms import Searchform, CommentForm, CommentEditForm, ResponseForm
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import Q
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from cards.models import MajorArcana, MinorArcana, Corte




def home(request): 
    img = Home.objects.all()
    return render(request, 'post/home.html', {'img': img})


def post_list(request):
    posts = Post.published.all() 
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number) 
    except PageNotAnInteger: 
          page_obj = paginator.get_page(1)
    except EmptyPage:        
        page_obj = paginator.get_page(paginator.num_pages)      
    return render(request, 'post/post_list.html', {'page_obj': page_obj})


def category_list(request): 
    categorys = Category.objects.all().order_by('name')
    print(categorys)
    return render(request, 'post/category_list.html', {'categorys':categorys})

    
def post_detail(request, year, month, day, id, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post, created__year=year, created__month=month, created__day=day, id=id)
    comments = post.post_comments.filter(active=True)
    comment_form = CommentForm()
    return render(request, 'post/post_detail.html', {'post': post, 'comment_form': comment_form , 'comments': comments})

def post_category(request, category_id):
    posts = Post.objects.filter(category_id=category_id, status=Post.Status.PUBLISHED)
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number) 
    except PageNotAnInteger: 
          page_obj = paginator.get_page(1)
    except EmptyPage:        
        page_obj = paginator.get_page(paginator.num_pages)  
    return render(request, 'post/post_category.html', {'page_obj': page_obj})


def post_search(request):
    form = Searchform()
    query = None
    results1 = []
    results2 = []
    results3 = []
    results4 = []

    if 'query' in request.GET:
        form = Searchform(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']            
            results1 = Post.published.filter(Q(title__icontains=query) | Q(body_post__icontains=query)).order_by('-created')
            results2 = MajorArcana.objects.filter(Q(name_major_arcana__icontains=query) | Q(description__icontains=query))
            results3 = MinorArcana.objects.filter(Q(name_minor_arcana__icontains=query) | Q(description__icontains=query)).order_by('icone')
            results4 = Corte.objects.filter(Q(name_corte__icontains=query) | Q(description__icontains=query)).order_by('icone')
        return render(request, 'post/search.html', {'form': form, 'query': query, 'results1': results1, 'results2':results2, 'results3':results3 , 'results4':results4})



@login_required
def post_comment(request, post_id):    
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    new_comment = None
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post_comment = post
            new_comment.user_comment = request.user 
            new_comment.save()
            messages.success(request, 'Comentário adicionado com sucesso!')
            return redirect('post:post_detail', year=post.created.year, month=post.created.month, day=post.created.day, id=post.id, post=post.slug)
        else:
            messages.error(request, 'Erro ao adicionar o comentário')
    responses = Response.objects.filter(response_comment__post_comment=post, active=True)
    for response in responses:
        print(f'Resposta: {response.body_response}')
    return render(request, 'post/post_detail.html', {'post': post, 'form': form, 'new_comment': new_comment, 'responses': responses})

@login_required
def comment_delete(request, post_id, comment_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = get_object_or_404(Comment, id=comment_id, active=True)
    if request.method == 'POST':
        if request.user == comment.user_comment: 
            comment.delete()
            messages.success(request, 'Comentário excluído com sucesso!')
        return redirect('post:post_detail', year=post.created.year, month=post.created.month, day=post.created.day, id=post.id, post=post.slug)

@login_required
def comment_edit(request, post_id, comment_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = get_object_or_404(Comment, id=comment_id, active=True)    
    if request.method == 'POST':        
        if request.user == comment.user_comment:
            form = CommentEditForm(data=request.POST, instance=comment)
            if form.is_valid():
                form.save()
                messages.success(request, 'Comentário editado com sucesso!')
            return redirect('post:post_detail', year=post.created.year, month=post.created.month, day=post.created.day, id=post.id, post=post.slug)


@login_required
def response_comment(request, post_id, comment_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = get_object_or_404(Comment, id=comment_id, active=True) 
    new_response = None
    form = ResponseForm()

    if request.method == 'POST':
        form = ResponseForm(data=request.POST)
        if form.is_valid():
            new_response = form.save(commit=False)
            new_response.response_comment = comment
            new_response.user_response = request.user
            new_response.save()
            messages.success(request, 'Resposta adicionada com sucesso!')
            return redirect('post:post_detail', year=post.created.year, month=post.created.month, day=post.created.day, id=post.id, post=post.slug)
        else:
            messages.error(request, 'Erro ao adicionar a resposta')

    return render(request, 'post/post_detail.html', {'post': post, 'form': form, 'new_response': new_response})


def contribua(request):
    return render(request, 'post/contribua.html')