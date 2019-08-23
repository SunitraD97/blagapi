from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from .models import Comment, Post, Vote

class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = User
            fields = ('username', 'email', 'password')
            extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = User(
                email=validated_data['email'],
                username=validated_data['username']
            )
            user.set_password(validated_data['password'])
            user.save()
            Token.objects.create(user=user)
            return user

class VoteSerializer(serializers.ModelSerializer):
    class Mdeta:
        models = Vote
        fields = '__all__'
    

class CommentSerializer(serializers.ModelSerializer):
    vote = VoteSerializer(many=True, required=False)

    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Post
        fields = '__all__'


