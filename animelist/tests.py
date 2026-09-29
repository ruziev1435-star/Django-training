from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Anime, Feedback, Post


class PageTests(TestCase):
    def test_pages_load(self):
        for name in ['animelist:home', 'animelist:post', 'animelist:feedback']:
            with self.subTest(name=name):
                response = self.client.get(reverse(name))
                self.assertEqual(response.status_code, 200)

    def test_nav_links_point_to_real_pages(self):
        response = self.client.get(reverse('animelist:home'))
        for url in ['/', '/posts/', '/feedback/']:
            self.assertContains(response, f'href="{url}"')

    def test_posts_are_listed_newest_first(self):
        Post.objects.create(title='Older post', content='a', author='x')
        Post.objects.create(title='Newer post', content='b', author='y')
        response = self.client.get(reverse('animelist:post'))
        self.assertEqual(
            [p.title for p in response.context['posts']],
            ['Newer post', 'Older post'],
        )

    def test_posts_page_shows_empty_message(self):
        response = self.client.get(reverse('animelist:post'))
        self.assertContains(response, 'No posts yet')


class FeedbackFormTests(TestCase):
    url = reverse('animelist:feedback')

    def test_valid_feedback_is_saved(self):
        response = self.client.post(self.url, {
            'title': 'Great site',
            'submitted_by': 'Ruslan',
            'email': '',
            'content': 'Keep it up',
        }, follow=True)
        self.assertRedirects(response, reverse('animelist:home'))
        self.assertContains(response, 'Your feedback has been sent')
        feedback = Feedback.objects.get()
        self.assertEqual(feedback.title, 'Great site')
        self.assertIsNone(feedback.anime)
        self.assertEqual(str(feedback), 'Ruslan: Great site')

    def test_feedback_about_an_anime_saves_email(self):
        anime = Anime.objects.create(
            title='Bleach', publication_date=date(2004, 10, 5), rating='9.0'
        )
        self.client.post(self.url, {
            'title': 'Love it',
            'anime': anime.pk,
            'submitted_by': 'Ruslan',
            'email': 'me@example.com',
            'content': 'Top 1',
        })
        feedback = Feedback.objects.get()
        self.assertEqual(feedback.anime, anime)
        self.assertEqual(feedback.email, 'me@example.com')
        self.assertEqual(str(feedback), 'Ruslan on Bleach')

    def test_missing_title_shows_custom_error(self):
        response = self.client.post(self.url, {
            'title': '', 'submitted_by': 'Ruslan', 'content': 'x',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please, enter a title')
        self.assertFalse(Feedback.objects.exists())

    def test_help_text_is_shown(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'refrain from using any offensive language')
