from rest_framework import serializers
from .models import Test, Person

class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = ('weather','temperature','driver','location',
                'track', 'fast_lap', 'tires', 'tire_condition',
                'engine', 'software', 'comments','created_at','personnel')

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('email', 'name', 'subteam', 'phone', 'licensed')
        