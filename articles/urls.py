from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('create/', views.author_create, name='create'),
    path('form/', views.article_form, name='form'),
    path('detail/<int:pk>/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.article_detail, name='detail'),
    path('delete/<int:pk>', views.article_delete, name='delete'),
]
