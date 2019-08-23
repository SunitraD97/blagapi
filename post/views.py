from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Post, Comment

def post_list(request):
    MAX_OBJECTS = 20
    post = Post.objects.all()[:20]
    data = {"results": list(post.values("pk", "post", "post_by__username", "pub_date"))}
    return JsonResponse(data)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = {"results": {
        "post": post.post,
        "post_by": post.post_by.username,
        "pub_date": post.pub_date
    }}
    return JsonResponse(data)

def comment_list(request):
    MAX_OBJECTS = 20
    comment = Comment.objects.all()[:20]
    data = {"results": list(comment.values("pk", "comment", "image_comment", "comment_date","comment_by__username"))}
    return JsonResponse(data)

def comment_detail(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    data = {"results": {
        "comment": comment.comment,
        "comment_by": comment.comment_by.username,
        "comment_date": comment.mment_date
    }}
    return JsonResponse(data)