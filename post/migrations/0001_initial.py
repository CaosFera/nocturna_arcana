# Generated by Django 5.0.3 on 2024-05-07 19:10

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(upload_to='logos/')),
                ('img2', models.ImageField(upload_to='logos/')),
                ('img3', models.ImageField(upload_to='logos/')),
                ('img4', models.ImageField(upload_to='logos/')),
            ],
        ),
        migrations.CreateModel(
            name='SiteLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logos/')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Título')),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Imagem')),
                ('body_post', ckeditor.fields.RichTextField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atualizado')),
                ('status', models.CharField(choices=[('DF', 'Rascunho'), ('PB', 'Publicado')], default='PB', max_length=2, verbose_name='Status')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='post_category', to='post.category')),
                ('user_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_comment', models.TextField(verbose_name='Texto')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atualizado')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('user_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL)),
                ('post_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='post.post')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_response', models.TextField(verbose_name='Texto')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atualizado')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('response', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_response', to='post.response')),
                ('response_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_responses', to='post.comment')),
                ('user_response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_response', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['-created'], name='post_post_created_27aeb6_idx'),
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['-created'], name='post_commen_created_409d9a_idx'),
        ),
        migrations.AddIndex(
            model_name='response',
            index=models.Index(fields=['-created'], name='post_respon_created_c8a67f_idx'),
        ),
    ]