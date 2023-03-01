from men.models import Men, Category


def get_all_men():
    return Men.objects.filter(is_published=True).select_related('cat')


def get_men_by_category(object):
    return Men.objects.filter(cat__slug=object.kwargs['cat_slug'], is_published=True).select_related('cat')


def get_categories(object):
    return Category.objects.filter(slug=object.kwargs['cat_slug'])


def get_category_title(object, context, cat):
    return f"Отображение по рубрике: {context['posts'][0].cat}"


def get_selected_cat(object, context):
    return context['posts'][0].cat_id
