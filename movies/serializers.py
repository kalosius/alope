from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(label="Enter Movie Id")
    title = serializers.CharField(label="Enter Movie title")
    description = serializers.CharField(label="Enter description")