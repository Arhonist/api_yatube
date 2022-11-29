from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from posts.models import Post, Group, Comment, User
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    """def perform_update(self, serializer):
        instance = self.get_object()
        if self.request.user != instance.author:
            return Response(status=status.HTTP_403_FORBIDDEN)
        updated_instance = serializer.save()"""
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user != instance.author:
            return Response(status=status.HTTP_403_FORBIDDEN)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PostSerializer(instance, data=request.data, partial=True)
        if request.user != instance.author:
            return Response(status=status.HTTP_403_FORBIDDEN)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
