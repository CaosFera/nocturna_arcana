from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Tarot(models.Model):
    title = models.CharField("Título", max_length=100)
    image_tarot = models.ImageField("Imagem", upload_to='cards/')
    text_body = RichTextField("Descrição") 

    def __str__(self):
        return f"{self.title}"  



class MajorArcana(models.Model):
    MAJOR_CHOICES = [
    ("0 - O Louco", "0 - O Louco"),
    ("1 - O Mago", "1 - O Mago"),
    ("2 - A Sacerdotisa", "2 - A Sacerdotisa"),
    ("3 - A Imperatriz", "3 - A Imperatriz"),
    ("4 - O Imperador", "4 - O Imperador"),
    ("5 - O Hierofante", "5 - O Hierofante"),
    ("6 - Os Amantes", "6 - Os Amantes"),
    ("7 - A Carruagem", "7 - A Carruagem"),
    ("8 - A Justiça", "8 - A Justiça"),
    ("9 - O Eremita", "9 - O Eremita"),
    ("10 - A Roda da Fortuna", "10 - A Roda da Fortuna"),
    ("11 - A Força", "11 - A Força"),
    ("12 - O Enforcado", "12 - O Enforcado"),
    ("13 - A Morte", "13 - A Morte"),
    ("14 - A Temperança", "14 - A Temperança"),
    ("15 - O Diabo", "15 - O Diabo"),
    ("16 - A Torre", "16 - A Torre"),
    ("17 - A Estrela", "17 - A Estrela"),
    ("18 - A Lua", "18 - A Lua"),
    ("19 - O Sol", "19 - O Sol"),
    ("20 - O Julgamento", "20 - O Julgamento"),
    ("21 - O Mundo", "21 - O Mundo"),
]



    name_major_arcana = models.CharField("Nome", max_length=30, choices=MAJOR_CHOICES)  
    slug = models.SlugField("Slug", max_length=200, blank=True)  
    description = RichTextField("Descrição") 
    image_major = models.ImageField("Imagem", upload_to='cards/')   
    key_word_major = TaggableManager("Palavras Chave")
    

    class Meta:
        ordering = ['name_major_arcana']
        indexes = [
            models.Index(fields=['name_major_arcana']),
        ]

    def __str__(self):
        return f"{self.name_major_arcana}"  
    

    def get_absolute_url(self):
        return reverse('cards:major_arcana_detail', kwargs={'slug': self.slug})




class MinorArcana(models.Model):
    ICONE_CHOICES = [
    ("fas fa-wand", "Paus"),
    ("fas fa-trophy", "Cálice"),
    ("fas fa-sword", "Espadas"),
    ("fas fa-coin", "Moeda"),
    ]    

    MINOR_CHOICES = [
    ("Às de Paus", "Às de Paus"),
    ("Dois de Paus", "Dois de Paus"),
    ("Três de Paus", "Três de Paus"),
    ("Quatro de Paus", "Quatro de Paus"),
    ("Cinco de Paus", "Cinco de Paus"),
    ("Seis de Paus", "Seis de Paus"),
    ("Sete de Paus", "Sete de Paus"),
    ("Oito de Paus", "Oito de Paus"),
    ("Nove de Paus", "Nove de Paus"),
    ("Dez de Paus", "Dez de Paus"),
    ("Às de Copas", "Às de Copas"),
    ("Dois de Copas", "Dois de Copas"),
    ("Três de Copas", "Três de Copas"),
    ("Quatro de Copas", "Quatro de Copas"),
    ("Cinco de Copas", "Cinco de Copas"),
    ("Seis de Copas", "Seis de Copas"),
    ("Sete de Copas", "Sete de Copas"),
    ("Oito de Copas", "Oito de Copas"),
    ("Nove de Copas", "Nove de Copas"),
    ("Dez de Copas", "Dez de Copas"),
    ("Às de Espadas", "Às de Espadas"),
    ("Dois de Espadas", "Dois de Espadas"),
    ("Três de Espadas", "Três de Espadas"),
    ("Quatro de Espadas", "Quatro de Espadas"),
    ("Cinco de Espadas", "Cinco de Espadas"),
    ("Seis de Espadas", "Seis de Espadas"),
    ("Sete de Espadas", "Sete de Espadas"),
    ("Oito de Espadas", "Oito de Espadas"),
    ("Nove de Espadas", "Nove de Espadas"),
    ("Dez de Espadas", "Dez de Espadas"),
    ("Às de Ouros", "Às de Ouros"),
    ("Dois de Ouros", "Dois de Ouros"),
    ("Três de Ouros", "Três de Ouros"),
    ("Quatro de Ouros", "Quatro de Ouros"),
    ("Cinco de Ouros", "Cinco de Ouros"),
    ("Seis de Ouros", "Seis de Ouros"),
    ("Sete de Ouros", "Sete de Ouros"),
    ("Oito de Ouros", "Oito de Ouros"),
    ("Nove de Ouros", "Nove de Ouros"),
    ("Dez de Ouros", "Dez de Ouros"),
]


    icone = models.CharField("Ícone", max_length=20, choices=ICONE_CHOICES)    
    name_minor_arcana  = models.CharField("Nome", max_length=20, choices=MINOR_CHOICES, unique=True)
    slug = models.SlugField("Slug")
    description = RichTextField("Descrição")    
    image_minor = models.ImageField("Imagem", upload_to="cards/")
    key_word_minor = TaggableManager("Palavras Chave")
    

    class Meta:
        ordering = ['name_minor_arcana']
        indexes = [
            models.Index(fields=['name_minor_arcana']),
        ]

    def __str__(self):
        return f"{self.name_minor_arcana}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_minor_arcana)            
        super().save(*args, **kwargs)   


    def get_absolute_url(self):
        return reverse('cards:enumerators_detail', kwargs={'slug': self.slug})   

    def order(self):
        CASE_SQL = "(CASE name_minor_arcana " \
                "WHEN 'Às de Paus' THEN 1 " \
                "WHEN 'Dois de Paus' THEN 2 " \
                "WHEN 'Três de Paus' THEN 3 " \
                "WHEN 'Quatro de Paus' THEN 4 " \
                "WHEN 'Cinco de Paus' THEN 5 " \
                "WHEN 'Seis de Paus' THEN 6 " \
                "WHEN 'Sete de Paus' THEN 7 " \
                "WHEN 'Oito de Paus' THEN 8 " \
                "WHEN 'Nove de Paus' THEN 9 " \
                "WHEN 'Dez de Paus' THEN 10 " \
                "WHEN 'Às de Copas' THEN 11 " \
                "WHEN 'Dois de Copas' THEN 12 " \
                "WHEN 'Três de Copas' THEN 13 " \
                "WHEN 'Quatro de Copas' THEN 14 " \
                "WHEN 'Cinco de Copas' THEN 15 " \
                "WHEN 'Seis de Copas' THEN 16 " \
                "WHEN 'Sete de Copas' THEN 17 " \
                "WHEN 'Oito de Copas' THEN 18 " \
                "WHEN 'Nove de Copas' THEN 19 " \
                "WHEN 'Dez de Copas' THEN 20 " \
                "WHEN 'Às de Espadas' THEN 21 " \
                "WHEN 'Dois de Espadas' THEN 22 " \
                "WHEN 'Três de Espadas' THEN 23 " \
                "WHEN 'Quatro de Espadas' THEN 24 " \
                "WHEN 'Cinco de Espadas' THEN 25 " \
                "WHEN 'Seis de Espadas' THEN 26 " \
                "WHEN 'Sete de Espadas' THEN 27 " \
                "WHEN 'Oito de Espadas' THEN 28 " \
                "WHEN 'Nove de Espadas' THEN 29 " \
                "WHEN 'Dez de Espadas' THEN 30 " \
                "WHEN 'Às de Ouros' THEN 31 " \
                "WHEN 'Dois de Ouros' THEN 32 " \
                "WHEN 'Três de Ouros' THEN 33 " \
                "WHEN 'Quatro de Ouros' THEN 34 " \
                "WHEN 'Cinco de Ouros' THEN 35 " \
                "WHEN 'Seis de Ouros' THEN 36 " \
                "WHEN 'Sete de Ouros' THEN 37 " \
                "WHEN 'Oito de Ouros' THEN 38 " \
                "WHEN 'Nove de Ouros' THEN 39 " \
                "WHEN 'Dez de Ouros' THEN 40 " \
                "END)"
        return MinorArcana.objects.extra(select={'minor_order': CASE_SQL}, order_by=['minor_order'])


class Corte(models.Model):
    ICONE_CHOICES = [
    ("fas fa-wand", "Paus"),
    ("fas fa-trophy", "Cálice"),
    ("fas fa-sword", "Espadas"),
    ("fas fa-coin", "Moeda"),
    ]


    CORTE_CHOICES = [

    ("Pajem de Paus", "Pajem de Paus"),
    ("Cavaleiro de Paus", "Cavaleiro de Paus"),
    ("Rainha de Paus", "Rainha de Paus"),
    ("Rei de Paus", "Rei de Paus"),
    ("Pajem de Copas", "Pajem de Copas"),
    ("Cavaleiro de Copas", "Cavaleiro de Copas"),
    ("Rainha de Copas", "Rainha de Copas"),
    ("Rei de Copas", "Rei de Copas"),
    ("Pajem de Espadas", "Pajem de Espadas"),
    ("Cavaleiro de Espadas", "Cavaleiro de Espadas"),
    ("Rainha de Espadas", "Rainha de Espadas"),
    ("Rei de Espadas", "Rei de Espadas"),
    ("Pajem de Ouros", "Pajem de Ouros"),
    ("Cavaleiro de Ouros", "Cavaleiro de Ouros"),
    ("Rainha de Ouros", "Rainha de Ouros"),
    ("Rei de Ouros", "Rei de Ouros"),

]


    icone = models.CharField("Ícone", max_length=20, choices=ICONE_CHOICES)    
    slug = models.SlugField(max_length=200, blank=True)
    name_corte = models.CharField("Nome", max_length=20, unique=True, choices=CORTE_CHOICES)
    image_corte = models.ImageField("Imagem", upload_to="cards/")
    description = RichTextField("Descrição")      
    key_word_minor = TaggableManager("Palavras Chave")
    

    class Meta:
        ordering = ['name_corte']
        indexes = [
            models.Index(fields=['name_corte']),
        ]

    def __str__(self):
        return f"{self.name_corte}"
    

    def get_absolute_url(self):
        return reverse('cards:corte_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_corte)
            print(f"Slug gerado automaticamente: {self.slug}")
        super().save(*args, **kwargs)   

    
    def order(self):
        CASE_SQL = "(CASE name_corte " \
                   "WHEN 'Pajem de Paus' THEN 1 " \
                   "WHEN 'Cavaleiro de Paus' THEN 2 " \
                   "WHEN 'Rainha de Paus' THEN 3 " \
                   "WHEN 'Rei de Paus' THEN 4 " \
                   "WHEN 'Pajem de Copas' THEN 5 " \
                   "WHEN 'Cavaleiro de Copas' THEN 6 " \
                   "WHEN 'Rainha de Copas' THEN 7 " \
                   "WHEN 'Rei de Copas' THEN 8 " \
                   "WHEN 'Pajem de Espadas' THEN 9 " \
                   "WHEN 'Cavaleiro de Espadas' THEN 10 " \
                   "WHEN 'Rainha de Espadas' THEN 11 " \
                   "WHEN 'Rei de Espadas' THEN 12 " \
                   "WHEN 'Pajem de Ouros' THEN 13 " \
                   "WHEN 'Cavaleiro de Ouros' THEN 14 " \
                   "WHEN 'Rainha de Ouros' THEN 15 " \
                   "WHEN 'Rei de Ouros' THEN 16 " \
                   "END)"
        return Corte.objects.extra(select={'corte_order': CASE_SQL}, order_by=['corte_order'])