from django.shortcuts import render, redirect
from firstapp.models import Article, Comment
from firstapp.form import CommentForm

# Create your views here.

def index(request):
    article_list = Article.objects.all()
    context = {}
    context["article_list"] = article_list
    return render(request, 'list.html', context)

def detail(request):

    if request.method == "GET":
        form = CommentForm 

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            content = form.cleaned_data["comment"]
            c = Comment(name=name, content=content)
            c.save()
            return redirect(to="detail")

    context = {}
    comment_list = Comment.objects.all()
    article = Article.objects.get(id=page_num)
    context['article'] = article
    context['comment_list'] = comment_list
    context['form'] = form
    return render(request, 'detail.html', context)