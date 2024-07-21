from rest_framework import serializers
from loginapp.models import Program, Course


class ProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Program
        fields = ['id', 'name']


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'name']
