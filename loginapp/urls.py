from rest_framework.routers import DefaultRouter

from loginapp.viewsets import CourseViewSet, ProgramViewSet, UserRegisterViewSet

router = DefaultRouter()
router.register('Course', CourseViewSet, basename='Course')
router.register('Program', ProgramViewSet, basename='Program')
router.register('UserRegister', UserRegisterViewSet, basename='UserRegister')

urlpatterns = router.urls
