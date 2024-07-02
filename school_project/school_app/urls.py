from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, ClassroomViewSet, SubjectViewSet, index

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'classrooms', ClassroomViewSet)
router.register(r'subjects', SubjectViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
]
