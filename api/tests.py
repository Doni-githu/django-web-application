from django.test import TestCase
from django.urls import reverse
from .models import Post


class BlogTests(TestCase):
    
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='password'
        )
        
        self.post = Post.objects.create(
            title='New Post',
            body='It is post body',
            author=self.user
        )
        
    def test_string_represetation(self):
        post = Post(title='Post mavzusi')
        self.assertEqual(str(post), post.title)
        
    def test_post_content(self):
        self.assertEqual(f'${self.post.title}', 'New Post')
        self.assertEqual(f'${self.post.author}', 'testuser')
        self.assertEqual(f'${self.post.body}', 'It is post body')
    def test_post_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Post matni')
        self.assertTemplateUsed(response, 'home.html')
        
    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'New Post')
        self.assertTemplateUsed(response, 'post_detail.html')