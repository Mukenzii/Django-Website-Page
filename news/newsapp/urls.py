from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name='index'),
    path('', ArticleList.as_view(), name='index'),
    path('category/<int:category_id>', ArticlesByCategory.as_view(), name='category'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
    path('search/', search, name='search')
]