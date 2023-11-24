from rest_framework import serializers

class PopSerializer(serializers.Serializer):
    id = serializers.IntegerField(label="Enter Song Id")
    artist = serializers.CharField(label="Enter artist name")
    title = serializers.CharField(label="Enter Song title")