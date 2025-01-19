from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    path('create_author/', views.author_create, name='create_author'),
    path('create_article/', views.article_create, name='create_article'),
    path('detail/<int:pk>/', views.article_detail, name='detail'),
    path('confirmation/<int:pk>/', views.comment_confirmation, name='confirmation'),
    path('delete/<int:pk>/', views.article_delete, name='delete'),
]