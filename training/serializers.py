from rest_framework import serializers
from training.models import Provider, Category, Package, Lesson
from rest_framework.reverse import reverse

class ProviderSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    class Meta:
        model = Provider
        fields = ('id','name', 'icon','links')

    def get_links(self, obj):
        request = self.context['request']
        return {'self': reverse('provider-detail', kwargs={'pk': obj.pk}, request=request),}

class CategorySerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ('id','name', 'parent','links')

    def get_links(self, obj):
        request = self.context['request']
        links = {'self': reverse('category-detail', kwargs={'pk': obj.pk}, request=request),}
        packages_link = []
        packages = Package.objects.filter(category=obj.pk).all().values('id','name')
        if packages:
            for i in packages:
                packages_link.append({'package': i['name'], 'url':reverse('package-detail', kwargs={'pk': i['id']}, request=request)})

        links['packages'] = packages_link
        # links['packages'] = reverse('package-detail', kwargs={'pk': obj.pk}, request=request)

        return links

class PackageSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    class Meta:
        model = Package
        fields = ('id','name', 'photo','price', 'discount', 'provider', 'description', 'level', 'is_enable','links')
    def get_links(self, obj):
        request = self.context['request']
        links = {'self': reverse('package-detail', kwargs={'pk': obj.pk}, request=request),}
        return links

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id','name', 'package', 'order')
