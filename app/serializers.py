from rest_framework.serializers import ModelSerializer
from app.models import Image


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image', 'getting_time', 'time_of_end_converting_job')