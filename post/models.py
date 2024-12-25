from django.db import models
from django.conf import settings 
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField("Categoria", max_length=70)
    
    def get_absolute_url(self):
        return reverse('post:post_category', args=[self.pk])

    def __str__(self):
        return self.name


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class CategoryManager(models.Manager):
    def category_queryset(self):
        return super().get_queryset().filter(post_category__status=Post.Status.PUBLISHED)

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Rascunho'
        PUBLISHED = 'PB', 'Publicado'

        
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post_category', default=None)
    user_post = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_posts')
    title = models.CharField("Título", max_length=80)
    slug = models.SlugField(max_length=200, blank=True)
    image = models.ImageField("Imagem",  upload_to='images/%Y/%m/%d/')
    body_post = RichTextField()
    created = models.DateTimeField("Criado", auto_now_add=True)
    updated = models.DateTimeField("Atualizado", auto_now=True)
    status = models.CharField("Status", max_length=2, choices=Status.choices, default=Status.PUBLISHED)
    objects = models.Manager() 
    published = PublishedManager() 
    query_category = CategoryManager()
    
    def get_local_created(self):
        return timezone.localtime(self.created)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f"{self.title} - {self.user_post}"
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            print(f"Slug gerado automaticamente: {self.slug}")
        super().save(*args, **kwargs)   

    
    def get_absolute_url(self):
        return reverse('post:post_detail', args=[self.created.year, self.created.month, self.created.day, self.id, self.slug])


class Comment(models.Model):
    user_comment = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_comments')
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')     
    body_comment = models.TextField("Texto")
    created = models.DateTimeField("Criado", auto_now_add=True)
    updated = models.DateTimeField("Atualizado", auto_now=True)
    active = models.BooleanField("Ativo?", default=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f"{self.user_comment} - {self.post_comment.title}"

class Response(models.Model):
    response = models.ForeignKey('self', related_name='child_response', null=True, blank=True, on_delete=models.CASCADE)
    user_response = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_response')           
    response_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comments_responses')  
    body_response = models.TextField("Texto")
    created = models.DateTimeField("Criado",auto_now_add=True)
    updated = models.DateTimeField("Atualizado",auto_now=True)
    active = models.BooleanField("Ativo?",default=True)
    
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f"{self.user_response} - {self.response}"

      

class SiteLogo(models.Model):
    logo = models.ImageField(upload_to='logos/')

class Home(models.Model):
    img1 = models.ImageField(upload_to='logos/', blank=True)
    img2 = models.ImageField(upload_to='logos/', blank=True)
    img3 = models.ImageField(upload_to='logos/', blank=True)
    img4 = models.ImageField(upload_to='logos/', blank=True)
 