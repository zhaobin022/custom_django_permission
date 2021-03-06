from django.conf.urls import url, include
from rest_framework import routers
import rest_views as views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
# router.register(r'servers', views.ServerViewSet)
# router.register(r'servers', views.ServerViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^servers/', views.server_list),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]