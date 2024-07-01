# from django.test import TestCase
# from django.urls import reverse
# from django.contrib.auth.models import User
# from account.models import Profile, Rating
# from account.forms import RatingForm

# class CreateRatingTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='testpassword')
#         self.profile = Profile.objects.create(user=self.user, slug='test-profile')
#         self.rating_data = {
#             'rating': 5,  # Aqui você pode definir os dados da avaliação conforme necessário
#             # Adicione outros campos do formulário aqui, se houver
#         }
    
#     def test_create_rating_view(self):
#         # Simule uma requisição POST para a view create_rating
#         response = self.client.post(reverse('create_rating', kwargs={'slug': self.profile.slug}), data=self.rating_data)
#         self.assertEqual(response.status_code, 200)  # Verifique se a resposta é 200 OK
        
#         # Verifique se a avaliação foi criada corretamente
#         self.assertTrue(Rating.objects.filter(profile=self.profile, user=self.user, rating=self.rating_data['rating']).exists())
        
#         # Verifique se o campo avg_rating do perfil foi atualizado corretamente
#         updated_profile = Profile.objects.get(slug=self.profile.slug)
#         self.assertEqual(updated_profile.avg_rating, self.rating_data['rating'])
        
#         # Verifique se o formulário é exibido na página
#         self.assertIsInstance(response.context['form'], RatingForm)
