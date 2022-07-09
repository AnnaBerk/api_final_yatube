from rest_framework import viewsets

from django.shortcuts import get_object_or_404
from rest_framework import permissions

from posts.models import Post, Group, Follow
from .serializers import (PostSerializer, GroupSerializer,
                               CommentSerializer, FollowSerializer)
from .permissions import IsUserOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsUserOrReadOnly, permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsUserOrReadOnly]

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

class FollowViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer