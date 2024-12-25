from django.test import TestCase
from django.urls import reverse
from post.models import Category, Post, Comment, Response, SiteLogo, Home
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from PIL import Image
import io
import os
import shutil


class CategoryModelTest(TestCase):
    def setUp(self):
        # Cria uma instância de Category para ser usada em vários testes
        self.category = Category.objects.create(name='Tecnologia')

    def test_category_creation(self):
        # Verifica se a categoria foi criada corretamente
        self.assertEqual(self.category.name, 'Tecnologia')
        self.assertIsInstance(self.category, Category)
        self.assertEqual(str(self.category), 'Tecnologia')

    def test_category_str(self):
        # Verifica se o método __str__ retorna o nome da categoria
        self.assertEqual(str(self.category), 'Tecnologia')

    def test_get_absolute_url(self):
        # Verifica se o método get_absolute_url retorna a URL correta
        expected_url = reverse('post:post_category', args=[self.category.pk])
        self.assertEqual(self.category.get_absolute_url(), expected_url)


class PostModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.category1 = Category.objects.create(name='Test Category 1')
        self.category2 = Category.objects.create(name='Test Category 2')
        self.post1 = Post.objects.create(
            user_post=self.user,
            category=self.category1,
            title='Test Post 1',
            body_post='This is a test post.',
            status=Post.Status.PUBLISHED
        )

        self.post2 = Post.objects.create(
            user_post=self.user,
            category=self.category2,
            title='Test Post 2',
            body_post='Another test post.',
            status=Post.Status.PUBLISHED
        )

        self.post3 = Post.objects.create(
            user_post=self.user,
            category=self.category1,
            title='Test Post 3',
            body_post='Yet another test post.',
            status=Post.Status.DRAFT
        )

    def test_published_manager(self):
        published_posts = Post.published.all()
        self.assertEqual(published_posts.count(), 2)  # Update count to 2
        self.assertIn(self.post1, published_posts)
        self.assertIn(self.post2, published_posts)
        self.assertNotIn(self.post3, published_posts)

    def test_get_local_created(self):
        local_time = self.post1.get_local_created()
        self.assertEqual(local_time.tzinfo, timezone.get_current_timezone())

    def test_slug_creation_on_save(self):
        new_post = Post.objects.create(
            user_post=self.user,
            category=self.category1,
            title='Test Post 4',
            body_post='Yet another test post.',
            status=Post.Status.PUBLISHED
        )
        self.assertIsNotNone(new_post.slug)
        self.assertEqual(new_post.slug, 'test-post-4')

    def test_category_manager(self):
        category1_posts = Post.objects.filter(category=self.category1)
        self.assertEqual(category1_posts.count(), 2)
        self.assertIn(self.post1, category1_posts)
        self.assertNotIn(self.post2, category1_posts)
        self.assertIn(self.post3, category1_posts)


    
    

class CommentModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='TestCategory')
        self.user = User.objects.create(username='testuser')
        self.post = Post.objects.create(
            user_post=self.user,
            category=self.category,
            title='testpost',
            body_post='This is a test post.',
            status=Post.Status.PUBLISHED
        )
        self.comment = Comment.objects.create(user_comment=self.user, post_comment=self.post,
        body_comment = "conteudo do comentário", active=True)

    def test_comment_field(self):
        self.assertEqual(self.comment.user_comment.username, 'testuser')
        self.assertEqual(self.comment.post_comment.title, 'testpost')
        self.assertEqual(self.comment.body_comment, 'conteudo do comentário')
        self.assertIsNotNone(self.comment.created)
        self.assertIsNotNone(self.comment.updated)
        self.assertTrue(self.comment.active)

    def test_comment_str_method(self):
        expected_str = f"{self.comment.user_comment} - {self.comment.post_comment.title}"        
        self.assertEqual(str(self.comment), expected_str)


class SiteLogoModelTest(TestCase):    
    def setUp(self):        
        image = Image.new('RGB', (100, 100), color = (73, 109, 137))
        byte_arr = io.BytesIO()
        image.save(byte_arr, format='JPEG')
        self.test_image = SimpleUploadedFile(
            name='test_logo.jpg',
            content=byte_arr.getvalue(),
            content_type='image/jpeg'
        )

    def test_create_site_logo(self):
        # Criação do objeto SiteLogo
        site_logo = SiteLogo.objects.create(logo=self.test_image)
        # Verifique se o objeto foi criado corretamente
        self.assertIsNotNone(site_logo.id)
        # Verifique se o campo logo foi salvo corretamente
        self.assertTrue(os.path.exists(site_logo.logo.path))
        # Limpeza
        site_logo.logo.delete()

    def tearDown(self):
        # Remova apenas os arquivos de imagem de teste
        for path in self.test_image_paths:
            if os.path.exists(path):
                os.remove(path)

class HomeModelTest(TestCase):
    
    def setUp(self):
        # Criar imagens em memória
        self.test_images = []
        for i in range(1, 5):
            image = Image.new('RGB', (100, 100), color=(73, 109, 137))
            byte_arr = io.BytesIO()
            image.save(byte_arr, format='JPEG')
            uploaded_file = SimpleUploadedFile(
                name=f'test_img{i}.jpg',
                content=byte_arr.getvalue(),
                content_type='image/jpeg'
            )
            self.test_images.append(uploaded_file)

    def test_create_home_with_images(self):
        # Criação do objeto Home com as imagens simuladas
        home_instance = Home.objects.create(
            img1=self.test_images[0],
            img2=self.test_images[1],
            img3=self.test_images[2],
            img4=self.test_images[3]
        )

        # Verifica se o objeto foi criado corretamente
        self.assertIsNotNone(home_instance.id)

        # Verifica se os campos de imagem foram salvos corretamente
        self.assertTrue(os.path.exists(home_instance.img1.path))
        self.assertTrue(os.path.exists(home_instance.img2.path))
        self.assertTrue(os.path.exists(home_instance.img3.path))
        self.assertTrue(os.path.exists(home_instance.img4.path))

    def tearDown(self):
        # Remova apenas os arquivos de imagem de teste
        for path in self.test_image_paths:
            if os.path.exists(path):
                os.remove(path)