from django.conf.urls import url, include

from rest_framework import routers

from .views import UniversityViewSet, StudentViewSet



router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'universities', UniversityViewSet)



urlpatterns = router.urls