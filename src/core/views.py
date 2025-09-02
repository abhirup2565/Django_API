from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView  
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import PostSerializer
from .models import Post

# Create your views here.
class TestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,*args,**kwargs):
        qs = Post.objects.all()
        seralizer = PostSerializer(qs,many=True)
        return Response(seralizer.data)
    
    def post(self,request,*args,**kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)