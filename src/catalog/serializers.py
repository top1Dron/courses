from catalog.models import Course
from rest_framework import serializers


class CourseListSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(
        view_name='catalog:course_detail',
        lookup_field='id'
    )

    class Meta:
        model = Course
        fields = ['detail_url', 'name', 'start_date', 'end_date', 'lections_quantity']


class CourseDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = '__all__'