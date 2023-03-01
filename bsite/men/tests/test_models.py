from django.test import TestCase

from ..models import Men, Category


class MenModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Men.objects.create(title='Крисс Эванс',
                           slug='criss-evans',
                           content='Биография актера',
                           cat=Category.objects.create(name='Актеры'))

    def test_title_label(self):
        men = Men.objects.get(pk=1)
        field_label = men._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Заголовок')

    def test_cat_label(self):
        men = Men.objects.get(pk=1)
        field_label = men._meta.get_field('cat').verbose_name
        self.assertEquals(field_label, 'Категория')

    def test_title_max_length(self):
        men = Men.objects.get(pk=1)
        max_length = men._meta.get_field('title').max_length
        self.assertEquals(max_length, 125)

    def test_get_absolute_url(self):
        men = Men.objects.get(pk=1)
        self.assertEquals(men.get_absolute_url(), f'/post/criss-evans/')
