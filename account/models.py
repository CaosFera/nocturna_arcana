from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from django.db.models import CheckConstraint, Q, UniqueConstraint
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.utils import timezone
from django.db.models import Avg
from django.core.exceptions import ValidationError

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, blank=True)
    biographia = RichTextField()    
    photo = models.ImageField(upload_to="users")
    instagram = models.CharField("Instagram", max_length=200, null=True, blank=True, default='#')
    facebook = models.CharField("Facebook", max_length=200, null=True, blank=True, default='#')
    tiktok = models.CharField("Tik Tok", max_length=200, null=True, blank=True, default='#')
    telegram = models.CharField("Telegram", max_length=200, null=True, blank=True, default='#')
    whatsapp = models.CharField("WhatsApp", max_length=200, null=True, blank=True, default='#')
    average_rating = models.FloatField("Média", default=0)
    total_rating = models.IntegerField("Total de Avaliações", default=0)

    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'slug': self.slug})

    def get_profile_prices_url(self):
        return reverse('profile_prices', kwargs={'slug': self.slug})   

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)            
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username 
    
    def get_average_rating(self):
        return round(self.average_rating, 1)
       
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        permissions = [
            ('can_view_profile', 'Pode Ver Perfil'),
            ('can_change_profile', 'Pode Atualizar Perfil'),
            ('can_add_profile', 'Pode Adicionar Perfil'),
            ('can_delete_profile', 'Pode Deletar Perfil'),
        ]

class BannersProfile(models.Model):
    profile = models.ForeignKey(Profile, related_name='banners_profile', on_delete=models.CASCADE)
    banners = models.ImageField('Imagem', upload_to="banners/")

    def save(self, *args, **kwargs):
        if self.profile.banners_profile.count() >= 5:
            raise ValidationError("Você não pode adicionar mais de 5 banners.")
        super().save(*args, **kwargs)


    def __str__(self):
        return self.profile.user.username

class Rating(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_rating")
    comment = models.TextField("Comentário", null=False, blank=False)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=0)
    created = models.DateTimeField("Criado", auto_now_add=True)

    class Meta:
        constraints = [
            CheckConstraint(check=Q(rating__range=(0, 5)), name='valid_rate'),
            UniqueConstraint(fields=['user', 'profile'], name='unique_rating')
        ]
    
    
    def __str__(self):
        return str(self.rating)

    