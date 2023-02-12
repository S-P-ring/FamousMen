from django.urls import path, re_path
from .views import *

urlpatterns = [
    # path('', index, name='home'),
    path('category/<slug:cat_slug>/', MenCategory.as_view(), name='category'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('', MenHome.as_view(), name='home'),
    path('about/', about, name='about'),
    # path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    # path('post/<slug:post_slug>/', show_post, name='post'),
    # path('category/<slug:cat_slug>/', show_category, name='category')
]