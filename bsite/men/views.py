from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404

from .forms import AddPostForm
from .models import Men, Category


def index(request):
    posts = Men.objects.all()
    context = {
        'posts': posts,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'men/index.html', context=context)


def about(request):
    return render(request, 'men/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():

            try:
                Men.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка при добавление нового поста')

    else:
        form = AddPostForm()
    return render(request, 'men/addpage.html', {'title': 'Добавление статьи', 'form': form})


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def show_post(request, post_slug):
    post = get_object_or_404(Men, slug=post_slug)
    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'men/post.html', context=context)


def show_category(request, cat_slug):
    posts = Men.objects.filter(cat__slug=cat_slug)
    cat = Category.objects.filter(slug=cat_slug)
    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'title': f'Отображение по рубрике: "{cat[0].name}"',
        'cat_selected': cat_slug,
    }

    return render(request, 'men/index.html', context=context)
