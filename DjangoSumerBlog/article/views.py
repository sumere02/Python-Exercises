from django.shortcuts import render,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from django.contrib import messages
from .models import Article,Comment
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")

@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context)
@login_required(login_url="user:login")
def addarticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()
        messages.info(request,"Article Added")
        return redirect("article:dashboard")
    context = {
        "form":form
    }
    return render(request,"addarticle.html",context)
def detail(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id)
    comments = article.comments.all()
    context = {
        "article":article,
        "comments":comments
    }
    return render(request,"detail.html",context)
@login_required(login_url="user:login")
def update(request,id):
    instance_article = get_object_or_404(Article,id = id)
    article = ArticleForm(request.POST or None,request.FILES or None,instance = instance_article)
    context = {
        "article":article
    }
    if article.is_valid():
        instance_article = article.save(commit = False)
        instance_article.author = request.user
        instance_article.save()
        messages.info(request,"Article Updated")
        return redirect("article:dashboard")
    else:
        return render(request,"update.html",context)
@login_required(login_url="user:login")
def delete(request,id):
    article = get_object_or_404(Article, id = id)
    article.delete()
    messages.info(request,"Article Deleted")
    return redirect("article:dashboard")

def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
    else:
        articles = Article.objects.all()
    context = {
        "articles":articles
    }
    return render(request,"articles.html",context)

def comment(request,id):
    article = get_object_or_404(Article,id = id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Comment(article = article,comment_author = comment_author,comment_content = comment_content)
        newComment.save()
        return redirect("../../article/" + str(id))