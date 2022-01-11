from rest_framework import serializers 
from news.models import Article

class ArticleSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    main_text = serializers.CharField()
    published_time = serializers.DateField()
    is_active = serializers.BooleanField()
    created_time = serializers.DateTimeField(read_only=True)
    updated_time = serializers.DateTimeField(read_only=True)


    def create(self,validated_data):
        return Article.objects.create(**validated_data) 

    def update(self,validated_data,instance,):
        instance.author = validated_data.get('author',instance.author)
        instance.title = validated_data.get('title',instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.main_text = validated_data.get('main_text',instance.main_text)
        instance.published_time = validated_data.get('published_time',instance.published_time)
        instance.is_active = validated_data.get('is_active',instance.is_active)
        instance.save()
        return instance
         