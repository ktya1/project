from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from posts.forms import PostForm
from posts.models import Post


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(
                title = form.cleaned_data['title'],
                text = form.cleaned_data['text'],
                author = request.user,
            )

            return redirect('list-posts')
    else:
        form = PostForm()

    return render(request, 'posts/create.html',  {'form': form})

def read_post(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    return render(request, 'posts/read.html',  {'post': post})



def list_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'posts/list.html', {'posts': posts})



def delete_post(request, post_id):
    post = get_object_or_404(Post, pk = post_id)

    if post.author != request.user:
        return HttpResponseForbidden('вы не можете удалить этот пост')

    if request.method == 'POST':
        post.delete()
        return redirect('list-posts')

    return render(request, 'posts/delete.html', {'post': post})




def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if post.author != request.user:
        return HttpResponseForbidden('Вы не можете редактировать этот пост')

    form = PostForm(initial={'title': post.title, 'text': post.text}) # при переходе будет форма с уже существующими данными 

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title_form = form.cleaned_data.get('title')
            text_form = form.cleaned_data.get('text')

            if title_form != '': 
                post.title = title_form

            if text_form != '':
                post.text = text_form

            post.save()
            return redirect('list-posts')
        
    return render(request, 'posts/update.html', {'form': form})

    