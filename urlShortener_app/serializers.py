from rest_framework.serializers import ModelSerializer


class urlShortenerSerializer(ModelSerializer):
    class Meta:
        model = 'urlShortener'
        fields = '__all__'