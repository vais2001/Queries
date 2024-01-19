from django.shortcuts import render

# Create your views here.
from rest_framework .views import APIView
from .models import*
from rest_framework.response import Response
from .serializers import*
from rest_framework import status
from django.db.models import Count,Sum
from django.db.models import Q

class GetStudent(APIView):
    serializer_class = StudentSerializer

    def get(self, request):
        get_alldata_student = Student.objects.all()
        get_single_object=Student.objects.get(id=2)
        get_icontains=get_alldata_student.filter(name__icontains='a')#for case insensitive
        get_contains=get_alldata_student.filter(name__contains='AK')#for case sensitive
        check_pk_id=get_alldata_student.filter(pk__in=[1,2,3])# return queryset which have pk value
        student_valuelist=get_alldata_student.values_list("name").get(id=2)#return a tupple ('vk',)
        student_valuelist=get_alldata_student.values_list("name",flat=True).get(id=2) #vk
        student_order=get_alldata_student.order_by("id")#for assecinding
        student_dassecinding_order=get_alldata_student.order_by("-id")#for dsc
        studentname_order=get_alldata_student.order_by("-id","name")[2]
        studentsbook_count =get_alldata_student.annotate(book_count=Count('books'))#for using models fields manipulate, addition ,counting 
        for student in studentsbook_count:
            print(f"Student: {student.name}, Book Count: {student.book_count}")
        logicaland=get_alldata_student.filter(Q(name="vk")&Q(address="rohta")) #true both condition
        logicalOr=get_alldata_student.filter(Q(name="vk")|Q(address="meerut"))#false one condition
        studentchoices=Student.objects.values_list("subjects").filter(subjects__in=('MATHS','COMPUTER')).annotate(Count('subjects'))
        studentchoices_withvalues=Student.objects.values("subjects").filter(subjects__in=('MATHS','COMPUTER')).annotate(count=Count('subjects'))       
        for stu in studentchoices_withvalues:
           print(f'{stu["subjects"]} count {stu["count"]}')

        reversedata=get_alldata_student.reverse()
        serialized_data = self.serializer_class(get_alldata_student, many=True).data
        return Response({"all_data": serialized_data})
    def post(self, request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data created"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BooksDetails(APIView):
  serializer_class=BooksSerializer
  
  def get(self,request):
    get_alldata_studentbooks=Books.objects.all()
    get_title=get_alldata_studentbooks.filter(genre="maths1")
    get_title=get_alldata_studentbooks.values_list("genre","title")
    get_startwith=get_alldata_studentbooks.filter(title__startswith='c', price__gte="350")
    connectwithforign=get_alldata_studentbooks.filter(student__name="ak")
    getstudentdata=Books.objects.select_related("student").values_list("student__name")
    selectrelated=Books.objects.select_related("student").values()
    prefetchrelated=Books.objects.prefetch_related("student").values()
    aggregatevalue=Books.objects.values_list("price").aaggregate(Sum("price"))#operation on one column 
    
    serialized_data = self.serializer_class(get_alldata_studentbooks, many=True).data
    return Response({"all_books": serialized_data})
  
  def post(self,request):
    serializer=BooksSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({"msg":"all_books details created"})
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      