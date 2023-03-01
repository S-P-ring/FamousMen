from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AddPostForm, RegisterUserForm, LoginUserForm, ContactForm
from .models import Men
from .services import get_men_by_category, get_all_men, get_categories, get_category_title, get_selected_cat


class MenHome(ListView):
    paginate_by = 3
    model = Men
    template_name = 'men/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return get_all_men()


class MenCategory(ListView):
    paginate_by = 3
    model = Men
    template_name = 'men/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = get_categories(self)
        context['title'] = get_category_title(object, context, cat)
        context['cat_selected'] = get_selected_cat(object, context)
        return context

    def get_queryset(self):
        return get_men_by_category(self)


class ShowPost(DeleteView):
    model = Men
    template_name = 'men/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'


class AddPage(LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'men/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')


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


# def contact(request):
#     return HttpResponse('Обратная связь')


# def login(request):
#     return HttpResponse('Авторизация')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'men/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        context['cat_selected'] = 0
        return context

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'men/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        context['cat_selected'] = 0
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'men/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обратная связь'
        context['cat_selected'] = 0
        return context

    def form_valid(self, form):
        return redirect('home')


def logout_user(request):
    logout(request)
    return redirect('login')

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
