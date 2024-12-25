


from django.test import TestCase
from account.models import Profile, Rating
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="Edivan")
        self.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'',
            content_type='image/jpeg'
        )
       
    def test_create_profile(self):
        profile = Profile.objects.create(
            user=self.user, 
            slug='edivan', 
            photo=self.test_image,
            biographia="biografia", 
            instagram="instagram", 
            facebook="facebook", 
            telegram="telegram", 
            tiktok="tiktok",
            whatsapp="whatsapp", 
            average_rating=4.5, 
            total_rating=10                                    
        )

        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.slug, 'edivan')
        self.assertTrue(profile.photo.name.startswith('users/test_image'))
        self.assertEqual(profile.instagram, 'instagram')
        self.assertEqual(profile.facebook, 'facebook')
        self.assertEqual(profile.telegram, 'telegram')
        self.assertEqual(profile.tiktok, 'tiktok')
        self.assertEqual(profile.whatsapp, 'whatsapp')
        self.assertEqual(profile.average_rating, 4.5)
        self.assertEqual(profile.total_rating, 10)

    def test_profile_absolute_url(self):  
        profile = Profile.objects.create(
            user=self.user, 
            slug='edivan', 
            photo=self.test_image,
            biographia="biografia", 
            instagram="instagram", 
            facebook="facebook", 
            telegram="telegram", 
            tiktok="tiktok",
            whatsapp="whatsapp", 
            average_rating=4.5, 
            total_rating=10                                    
        )

        expected_url = reverse('profile_detail', kwargs={'slug': profile.slug})
        self.assertEqual(profile.get_absolute_url(), expected_url)

    def test_profile_prices_url(self):  
        profile = Profile.objects.create(
            user=self.user, 
            slug='edivan', 
            photo=self.test_image,
            biographia="biografia", 
            instagram="instagram", 
            facebook="facebook", 
            telegram="telegram", 
            tiktok="tiktok",
            whatsapp="whatsapp", 
            average_rating=4.5, 
            total_rating=10                                    
        )

        expected_url = reverse('profile_prices', kwargs={'slug': profile.slug})
        self.assertEqual(profile.get_profile_prices_url(), expected_url)
    
    def test_profile_str_method(self):  
        profile = Profile.objects.create(
            user=self.user, 
            slug='edivan', 
            photo=self.test_image,
            biographia="biografia", 
            instagram="instagram", 
            facebook="facebook", 
            telegram="telegram", 
            tiktok="tiktok",
            whatsapp="whatsapp", 
            average_rating=4.5, 
            total_rating=10                                    
        )

        self.assertEqual(str(profile.user), "Edivan")

    def test_average_rating(self):  
        profile = Profile.objects.create(
            user=self.user, 
            slug='edivan', 
            photo=self.test_image,
            biographia="biografia", 
            instagram="instagram", 
            facebook="facebook", 
            telegram="telegram", 
            tiktok="tiktok",
            whatsapp="whatsapp", 
            average_rating=3.3333333333333335,
            total_rating=10                                    
        )

        self.assertAlmostEqual(profile.average_rating, 3.3, places=1)

    def test_verbose_name(self):
        verbose_name = Profile._meta.verbose_name
        self.assertEqual(verbose_name, 'Profile')

    def test_verbose_name_plural(self):
        verbose_name_plural = Profile._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, 'Profiles')

    def test_permissions(self):
        permissions = Profile._meta.permissions
        expected_permissions = [
            ('can_view_profile', 'Pode Ver Perfil'),
            ('can_change_profile', 'Pode Atualizar Perfil'),
            ('can_add_profile', 'Pode Adicionar Perfil'),
            ('can_delete_profile', 'Pode Deletar Perfil'),
        ]
        self.assertEqual(permissions, expected_permissions)