from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView

from .forms import AddPostForm
from .models import Men, Category


class MenHome(ListView):
    model = Men
    template_name = 'men/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Men.objects.filter(is_published=True)


class MenCategory(ListView):
    model = Men
    template_name = 'men/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = Category.objects.filter(slug=self.kwargs['cat_slug'])
        context['title'] = 'Отображение по рубрике: "' + str(context['posts'][0].cat) + '"'
        context['cat_selected'] = context['posts'][0].cat_id
        return context

    def get_queryset(self):
        return Men.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


class ShowPost(DeleteView):
    model = Men
    template_name = 'men/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'men/addpage.html'
    success_url = reverse_lazy('home')

def about(request):
    return render(request, 'men/about.html', {'title': 'О сайте'})


# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#
#     else:
#         form = AddPostForm()
#     return render(request, 'men/addpage.html', {'title': 'Добавление статьи', 'form': form})


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


# def index(request):
#     posts = Men.objects.all()
#     context = {
#         'posts': posts,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#     return render(request, 'men/index.html', context=context)


# def show_post(request, post_slug):
#     post = get_object_or_404(Men, slug=post_slug)
#     context = {
#         'post': post,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#     return render(request, 'men/post.html', context=context)


# def show_category(request, cat_slug):
#     print(cat_slug)
#     posts = Men.objects.filter(cat__slug=cat_slug)
#     cat = Category.objects.filter(slug=cat_slug)
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'title': f'Отображение по рубрике: "{cat[0].name}"',
#         'cat_selected': cat[0].pk,
#     }
#
#     return render(request, 'men/index.html', context=context)
