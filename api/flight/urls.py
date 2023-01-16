from rest_framework.routers import DefaultRouter
from .views import FlightViewSet, ReservationViewSet


router = DefaultRouter()
router.register('flights', FlightViewSet)
router.register('reservations', ReservationViewSet)

urlpatterns = router.urls
