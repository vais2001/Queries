from rest_framework import serializers
from .models import Student,Books


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
     model=Student
     fields=['name','address','subjects','phone_number']


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books    
        fields = '__all__'