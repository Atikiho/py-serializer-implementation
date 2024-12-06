import io

from django.db.migrations import serializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer_to_json = CarSerializer(car)
    return JSONRenderer().render(serializer_to_json.data)


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    return JSONParser().parse(stream)
