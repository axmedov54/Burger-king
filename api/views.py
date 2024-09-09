from django.shortcuts import render
from blog.models import Post
from .serializer import PostSerializers
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
# from .permissons import IAR




class Postlist(ListAPIView):
    # permission_classes=(IAR)
    queryset=Post.objects.all()
    serializer_class =PostSerializers

class Postruda(RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class =PostSerializers

class PostCrate(CreateAPIView):
    queryset=Post.objects.all()
    serializer_class =PostSerializers