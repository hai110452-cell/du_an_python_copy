from django.test import TestCase

class TemplateTest(TestCase):

    def test_template_used(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home/index.html')