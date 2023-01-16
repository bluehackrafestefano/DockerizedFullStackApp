from django.shortcuts import render
from .serializers import FlightSerializer, ReservationSerializer, StaffFlightSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Flight, Reservation
from .permissions import IsAdminOrReadOnly
from datetime import datetime, date
from django.db.models import Q


class FlightViewSet(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        serializer = super().get_serializer_class()
        if self.request.user.is_staff:
            return StaffFlightSerializer
        return serializer

    def get_queryset(self):
        queryset = super().get_queryset()

        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        today = date.today()

        if self.request.user.is_staff:
            return queryset
        else:
            return Flight.objects.filter(Q(date_of_departure__gt=today) | Q(date_of_departure=today, etd__gt=current_time))


class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        """
        This view should return a list of all the reservations
        for the currently authenticated user.
        """
        user = self.request.user
        return Reservation.objects.filter(user=user)
