from django.urls import path
from rest_framework.routers import DefaultRouter
from loginapp.viewsets import CourseViewSet, ProgramViewSet
from loginapp.views import RegisterView

router = DefaultRouter()
router.register('course', CourseViewSet, basename='course')
router.register('program', ProgramViewSet, basename='program')

urlpatterns = [
                  path('register/', RegisterView.as_view(), name='register'),
              ] + router.urls
