from django import forms
from django.core.exceptions import ValidationError

from .models import Men, Category


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Men
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

    def clean_title(self):
        """SQlite does not give an error
         about exceeding the string length,
         it just trims it"""

        title = self.cleaned_data['title']
        if len(title) > 255:
            raise ValidationError('Длина превышает 255 символов')
        return title