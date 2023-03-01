from django.test import TestCase

from ..models import Men, Category
from django.urls import reverse

class MenListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cat = Category.objects.create(name='Актеры', slug='actery')
        number_of_men = 13
        for men_num in range(number_of_men):
            Men.objects.create(title=f'{men_num}', slug = f'{men_num}',
                               content=f'{men_num}', cat=cat)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'men/index.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['men_list']) == 3)

    def test_lists_all_authors(self):
        resp = self.client.get(reverse('')+'?page=5')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['men_list']) == 1)