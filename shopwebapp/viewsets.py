from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer
from . import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework import viewsets
from . import models
# token Generated token 731e2b3b825d017bba1d374cb1869757e57b7e38 for user root
# Create your views here.
class ProductList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        product1 = Product.objects.all()
        serializer = ProductSerializer(product1, many=True)
        return Response(serializer.data)  
    def post(self):
        pass    
    

class CategoryList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        category1 = Category.objects.all()
        serializer = CategorySerializer(category1, many=True)
        return Response(serializer.data)  
    def post(self):
        pass