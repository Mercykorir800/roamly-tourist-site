from django.test import TestCase
from django.urls import reverse


class PublicPageTests(TestCase):
    def test_public_pages_render(self):
        pages = (
            ('home', 'home.html'),
            ('about', 'about.html'),
            ('contact', 'contact.html'),
        )

        for url_name, template_name in pages:
            with self.subTest(page=url_name):
                response = self.client.get(reverse(url_name))
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, template_name)
