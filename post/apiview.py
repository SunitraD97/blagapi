from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied

#from django.contrib.auth import authenticate
from .models import Post, Comment , Vote
from .serializers import UserSerializer, VoteSerializer, PostSerializer, CommentSerializer 



class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def destroy(self, request, *args, **kwargs):
        post = Post.objects.get(pk=self.kwargs["pk"])
        if not request.user == post.post_by:
            raise PermissionDenied("You cannot Post.")
        return super().destroy(request, *args, **kwargs)

class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.filter(post_id=self.kwargs["pk"])
        return queryset

    def post(self, request, *args, **kwargs):
        post =  Post.objects.get(pk=self.kwargs["pk"])
        if not request.user == post.post_by:
            raise PermissionDenied("You cannot Comment.")
        return super().post(request, *args, **kwargs)
    


class CreateVote(APIView):

    def post(self, request, pk, comment_pk):
        vote_by = request.data.get("vote_by")
        data = {'comment': comment_pk, 'post': pk, 'vote_by': vote_by}
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer