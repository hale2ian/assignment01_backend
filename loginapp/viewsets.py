from rest_framework import viewsets

from loginapp.models import Course, Program
from loginapp.serializers import CourseSerializer, ProgramSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class ProgramViewSet(viewsets.ModelViewSet):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
