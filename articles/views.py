from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Article, Comment


def home(request):
    articles = Article.objects.all()
    ctx = {'articles': articles }
    return render(request, 'index.html', ctx)

def author_create(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        biography = request.POST.get('biography')
        email = request.POST.get('email')
        if full_name and biography and email:
            Author.objects.create(
                full_name = full_name,
                biography = biography,
                email = email,
            )
            return redirect('articles:create_article')
    return render(request, 'articles/create-author.html')

def article_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        article_text = request.POST.get('article_text')
        author = request.POST.get('author')
        image = request.FILES.get('image')
        if title and article_text and author and image:
            author = Author.objects.get(id=author)
            Article.objects.create(
                title = title,
                article_text = article_text,
                author = author,
                image = image,
            )
            return redirect('home')
    authors = Author.objects.all()
    ctx = {'authors': authors }
    return render(request, 'articles/create-article.html', ctx)

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        if full_name and email and comment:
            Comment.objects.create(
                full_name = full_name,
                email = email,
                comment = comment,
                article = article,
            )
            return redirect('articles:confirmation', pk=pk)
    comments = article.comments.all()
    ctx = {'article': article, 'comments': comments,}
    return render(request, 'articles/blog-detail.html', ctx)

def comment_confirmation(request, pk):
    article = get_object_or_404(Article, pk=pk)
    ctx = {'article': article}
    return render(request,'articles/success-commented.html', ctx)

def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('home')





