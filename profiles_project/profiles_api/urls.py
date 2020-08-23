from django.conf.urls import url
from . import views
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('helloviewset', views.helloviewset, base_name= 'helloviewset')

urlpatterns = [
    url(r'^hellopythonview/',views.HelloApiView.as_view()),
    url(r'',include(router.urls))
]
