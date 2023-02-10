from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Men, Category


menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]


def index(request):
    posts = Men.objects.all()
    cats = Category.objects.all
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'men/index.html', context=context)

def about(request):
    return render(request, 'men/about.html',  {'menu': menu, 'title': 'О сайте'})

def addpage(request):
    return HttpResponse('Добавление статьи')

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')

def show_category(request, cat_id):
    posts = Men.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    cat = Category.objects.filter(pk=cat_id)
    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': f'Отображение по рубрике: "{cat[0].name}"',
        'cat_selected': cat_id,
    }

    return render(request, 'men/index.html', context=context)