from django.shortcuts import render, redirect, get_object_or_404
from articles.models import Author, Article, Comment


def home(request):
    articles = Article.objects.all()
    ctx = {'articles': articles}
    return render(request, 'index.html', ctx)

def author_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        biography = request.POST.get('biography')
        email = request.POST.get('email')
        if name and biography and email:
            Author.objects.create(
                name = name,
                biography = biography,
                email = email,
            )
            return redirect('articles:form')
    return render(request, 'articles/create-author.html')

def article_form(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        image = request.FILES.get('image')
        author = request.POST.get('author')
        if title and text and image and author:
            author = Author.objects.get(id=author)
            Article.objects.create(
                title = title,
                text = text,
                image = image,
                author = author,
            )
            return redirect('home')
    authors = Author.objects.all()
    ctx = {'authors': authors}
    return render(request, 'articles/create-article.html', ctx)


def article_detail(request, pk, year, month, day, slug):
    article = get_object_or_404(
        Article, pk=pk,
        created_at__year = year,
        created_at__month = month,
        created_at__day = day,
        slug=slug
    )
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        comment_text = request.POST.get('comment')
        your_email = request.POST.get('your_email')
        if first_name and comment_text and your_email:
            Comment.objects.create(
                first_name=first_name,
                comment=comment_text,
                your_email=your_email,
                article=article
            )
            return redirect('articles:detail', pk=pk, year=year, month=month, day=day, slug=slug)
    comments = article.comments.all()
    ctx = {'article': article, 'comments': comments,}
    return render(request, 'articles/blog-detail.html', ctx)


def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('home')
