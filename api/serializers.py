from rest_framework import serializers
from .models import *

class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    time = serializers.DateTimeField()
    slug = serializers.SlugField( max_length=250, null=True, blank=True, editable=False)
    text = serializers.CharField(max_length=500)

    def create(self, validated_data):
        return Post.object.create(validated_data)

    def update(self, instance, validated_data):
        instance.title =  validated_data.get('title', instance.title)
        instance.time = validated_data.get('time', instance.time)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.text = validated_data.get('text', instance.text)