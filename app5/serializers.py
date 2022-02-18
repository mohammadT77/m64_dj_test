from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    message = serializers.CharField(read_only=True)
    level = serializers.IntegerField(read_only=True)
    tags = serializers.CharField(read_only=True)  # "akbar asqar reza"
    level_tag = serializers.CharField(read_only=True)
    extra_tags = serializers.CharField(read_only=True)

