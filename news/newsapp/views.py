from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView
from .models import *
from django.db.models import Q
from django.contrib import messages


class ArticleList(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'newsapp/index.html'
    extra_context = {
        'title': "News Uz"
    }


class ArticlesByCategory(ArticleList):
    def get_queryset(self):
        return Article.objects.filter(category__id=self.kwargs['category_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = ArticleCategory.objects.get(id=self.kwargs['category_id']).title
        return context


class ArticleDetail(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'newsapp/article_detail.html'

    def get_queryset(self):
        return Article.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = self.get_queryset()[0].title
        context['articles'] = Article.objects.all()
        return context


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()

    context = {
        'form': form,
        'title': 'Log In'
    }
    return render(request, 'newsapp/login_form.html', context)


def user_logout(request):
    logout(request)
    return redirect('index')


def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('index')
    else:
        form = RegistrationForm()

    context = {
        'title': "Ro'yxatdan o'tish",
        'registration_form': RegistrationForm(),
        'form': form
    }
    return render(request, 'newsapp/register.html', context)


def search(request):
    word = request.GET.get('q')
    articles = Article.objects.filter(Q(title__icontains=word)|Q(content__icontains=word))
    context = {
        'articles': articles,
        'title': 'Qidiruv'
    }
    return render(request, 'newsapp/index.html', context)







