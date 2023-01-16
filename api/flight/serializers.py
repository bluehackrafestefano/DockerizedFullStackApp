from rest_framework import serializers
from .models import Flight, Reservation, Passenger


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    passenger = PassengerSerializer(many=True)
    flight = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    flight_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Reservation
        fields = (
            'id',
            'flight_id',
            'flight',
            'user_id',
            'user',
            'passenger',
        )

    def create(self, validated_data):
        passenger_data = validated_data.pop('passenger')
        validated_data['user_id'] = self.context.get('request').user.id
        reservation = Reservation.objects.create(**validated_data)

        for passenger in passenger_data:
            new_passenger = Passenger.objects.create(**passenger)
            reservation.passenger.add(new_passenger)

        reservation.save()
        return reservation


class StaffFlightSerializer(serializers.ModelSerializer):
    reservations_of_flight = ReservationSerializer(many=True, read_only=True)

    class Meta:
        model = Flight
        fields = (
            "id",
            "flight_number",
            "airlines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "etd",
            "reservations_of_flight",
        )