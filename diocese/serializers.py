from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from .models import CustomUser, Diocese, Bishop, Project, Parish, Priest, Chapel, MassSchedule, YouthGroup, YouthEvent, Diocese_Event, Blog



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class DioceseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diocese
        fields = '__all__'

class BishopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bishop
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ParishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parish
        fields = '__all__'

class PriestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Priest
        fields = '__all__'

class ChapelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapel
        fields = '__all__'

class MassScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MassSchedule
        fields = '__all__'

class YouthGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouthGroup
        fields = '__all__'

class YouthEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouthEvent
        fields = '__all__'

class DioceseEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diocese_Event
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

