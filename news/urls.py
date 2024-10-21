from django.urls import path

from news.views import index, categories_view, category_detail, news_detail

urlpatterns = [
    path('', index, name='home'),
    path('categories/', categories_view, name='categories_view'),
    path('categories/<int:id>/', category_detail, name='category_detail'),
    path('news/<str:slug>/', news_detail, name='detail_view'),
]