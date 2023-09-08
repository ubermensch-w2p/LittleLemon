from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BookingViewSet, MenuItemView, SingleMenuItemView, index

router = DefaultRouter()
router.register("tables", BookingViewSet)

urlpatterns = [
    path("", index, name="index"),
    path("menu/", MenuItemView.as_view(), name="menu-list"),
    path("menu/<int:pk>/", SingleMenuItemView.as_view(), name="menu-detail"),
    path("booking/", include(router.urls)),
]
