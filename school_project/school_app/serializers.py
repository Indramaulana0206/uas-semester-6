# school_app/serializers.py
from rest_framework import serializers
from .models import Student, Classroom, Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class ClassroomSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True)

    class Meta:
        model = Classroom
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    classroom = ClassroomSerializer()

    class Meta:
        model = Student
        fields = '__all__'
