from django.shortcuts import render, get_object_or_404

from .models import Post, Group


POST_NUM = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:POST_NUM]
    title = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'title': title,
        'text': 'Последние обновления на сайте',
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    gr_db = Group.objects.first()
    group_none = get_object_or_404(Group, slug=slug)
    posts = gr_db.group_posts.all().order_by('-pub_date')[:POST_NUM]
    title = 'Посты сообщества.'
    context = {
        'group': group_none,
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/group_list.html', context, slug)
