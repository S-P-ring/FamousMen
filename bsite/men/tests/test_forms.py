from django.core.exceptions import ValidationError
from django.test import TestCase

from ..forms import AddPostForm, RegisterUserForm
from ..models import Men, Category


class FormsTest(TestCase):
    def test_username_field_label(self):
        form = RegisterUserForm()
        self.assertTrue(form.fields['username'].label == 'Логин')

    def test_password2_field_label(self):
        form = RegisterUserForm()
        self.assertEqual(form.fields['password2'].label, 'Повтор пароля')

    def test_title_length(self):
        form = AddPostForm()
        cleaned_data = {}
        cleaned_data['title'] = ''.join([str(e) for e in range(258)])
        form.cleaned_data = cleaned_data
        self.assertRaises(ValidationError, form.clean_title)
