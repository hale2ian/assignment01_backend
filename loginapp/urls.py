from rest_framework.routers import DefaultRouter

from loginapp.viewsets import CourseViewSet, ProgramViewSet

router = DefaultRouter()
router.register('course', CourseViewSet, basename='course')
router.register('program', ProgramViewSet, basename='program')

urlpatterns = router.urls
