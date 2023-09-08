from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import BookingViewSet, MenuViewSet, index

router = DefaultRouter()
router.register("booking/tables", BookingViewSet)
router.register("menu", MenuViewSet)


urlpatterns = [
    path("", index, name="index"),
    path("", include(router.urls)),
    path("api-token-auth", obtain_auth_token),
]
