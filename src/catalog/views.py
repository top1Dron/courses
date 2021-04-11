from catalog.serializers import CourseListSerializer, CourseDetailSerializer
from catalog import services
from catalog.filters import CourseFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets, filters


class CourseListView(generics.ListCreateAPIView):
    queryset = services.get_all_cources()
    serializer_class = CourseListSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    filterset_class = CourseFilter


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = services.get_all_cources()
    serializer_class = CourseDetailSerializer
    lookup_url_kwarg = 'id'
    