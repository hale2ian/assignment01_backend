from rest_framework.routers import DefaultRouter

from loginapp.viewsets import CourseViewSet, ProgramViewSet, UserRegisterViewSet

router = DefaultRouter()
router.register('course', CourseViewSet, basename='course')
router.register('program', ProgramViewSet, basename='program')
router.register('userregister', UserRegisterViewSet, basename='userregister')

urlpatterns = router.urls
