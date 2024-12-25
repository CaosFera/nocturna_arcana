from django.shortcuts import render, get_object_or_404
from .models import MajorArcana, MinorArcana, Corte, Tarot
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from post.models import Home

def tarot_history(request):
    img = Home.objects.all()
    return render (request, 'cards/tarot_history.html', {'img':img})

def major_arcana_home(request):   
    tarot = Tarot.objects.first()
    majors = MajorArcana.objects.all()
    return render(request, 'cards/major_arcana_home.html', {'tarot':tarot, 'majors':majors})

def minor_arcana_home(request):       
    minors = MinorArcana.objects.all()
    return render(request, 'cards/minor_arcana_home.html', {'minors':minors})


def major_arcana_list(request):
    majors = MajorArcana.objects.all()
    paginator = Paginator(majors, 7)
    page_number = request.GET.get('page')    
    try:
        page_obj = paginator.get_page(page_number) 
    except PageNotAnInteger: 
          page_obj = paginator.get_page(1)
    except EmptyPage:        
        page_obj = paginator.get_page(paginator.num_pages)  
    return render(request, 'cards/major_arcana_list.html', {'page_obj':page_obj})

def major_arcana_detail(request, slug):
    major = get_object_or_404(MajorArcana, slug=slug)
    tags = major.key_word_major.all()  
    return render(request, 'cards/major_arcana_detail.html', {'major':major, 'tags':tags})




def minor_arcana(request):      
    return render(request, 'cards/minor_arcana.html')



def enumerators_list(request):
    minors = MinorArcana().order()
    paginator = Paginator(minors, 10)
    page_number = request.GET.get('page')    
    try:
        page_obj = paginator.get_page(page_number) 
    except PageNotAnInteger: 
          page_obj = paginator.get_page(1)
    except EmptyPage:        
        page_obj = paginator.get_page(paginator.num_pages)  
    return render(request, 'cards/enumerators_list.html', {'page_obj':page_obj})


def enumerators_detail(request, slug):       
    minor = get_object_or_404(MinorArcana, slug=slug)
    minors = MinorArcana.objects.filter(icone=minor.icone).order_by('icone')
    print(minors)
    return render(request, 'cards/enumerators_detail.html', {'minor':minor, 'minors':minors})


def corte_list(request):
    cortes = Corte().order()
    paginator = Paginator(cortes, 8)
    page_number = request.GET.get('page')    
    try:
        page_obj = paginator.get_page(page_number) 
    except PageNotAnInteger: 
          page_obj = paginator.get_page(1)
    except EmptyPage:        
        page_obj = paginator.get_page(paginator.num_pages)  
    return render(request, 'cards/corte_list.html', {'page_obj':page_obj})


def corte_detail(request, slug):
    corte = get_object_or_404(Corte, slug=slug)
    cortes = Corte().order()
    print(cortes)
    return render(request, 'cards/corte_detail.html', {'corte':corte, 'cortes':cortes})


