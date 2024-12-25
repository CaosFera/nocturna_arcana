# from django.test import TestCase, Client
# from django.urls import reverse
# from post.models import Post, Comment, Category, Response
# from django.contrib.auth.models import User

# class TestViews(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user(username='testuser', password='testpassword')
#         self.category = Category.objects.create(name='Test Category')
#         self.post = Post.objects.create(title='Test Post', body_post='Test Body', author=self.user, category=self.category)
#         self.comment = Comment.objects.create(body_comment='Test Comment', post_comment=self.post, user_comment=self.user)
#         self.response = Response.objects.create(body_response='Test Response', response_comment=self.comment, user_response=self.user)

#     def test_post_list_view(self):
#         response = self.client.get(reverse('post:post_list'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'post/post_list.html')

#     def test_post_detail_view(self):
#         response = self.client.get(reverse('post:post_detail', args=[self.post.created.year, self.post.created.month, self.post.created.day, self.post.slug]))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'post/post_detail.html')

#     def test_post_category_view(self):
#         response = self.client.get(reverse('post:post_category', args=[self.category.id]))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'post/post_category.html')

    