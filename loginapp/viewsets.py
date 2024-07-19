from rest_framework import viewsets

from loginapp.models import UserRegister, Course, Program
from loginapp.serializers import UserRegisterSerializer, CourseSerializer, ProgramSerializer


class UserRegisterViewSet(viewsets.ModelViewSet):
    serializer_class = UserRegisterSerializer
    queryset = UserRegister.objects.all()


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class ProgramViewSet(viewsets.ModelViewSet):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
