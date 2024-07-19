from rest_framework import serializers

from loginapp.models import Program, Course, UserRegister


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRegister
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'date_of_birth']


class ProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Program
        fields = ['name']


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['name']
