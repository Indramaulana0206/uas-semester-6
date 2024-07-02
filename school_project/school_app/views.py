# school_app/views.py
from rest_framework import viewsets
from .models import Student, Classroom, Subject
from .serializers import StudentSerializer, ClassroomSerializer, SubjectSerializer
# school_app/views.py
from django.shortcuts import render

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer



def index(request):
    return render(request, 'school_app/index.html')
