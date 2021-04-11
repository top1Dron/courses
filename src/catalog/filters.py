from catalog.models import Course
import django_filters as filters


class CourseFilter(filters.FilterSet):
    start_date = filters.DateFilter(lookup_expr='gte')
    end_date = filters.DateFilter(lookup_expr='lte')


    class Meta:
        model = Course
        fields = ['start_date', 'end_date']