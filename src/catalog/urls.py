from . import views
from django.urls import path


app_name = 'catalog'


urlpatterns = [
    path('', views.CourseListView.as_view(), name='courses_list'),
    path('<int:id>/', views.CourseDetailView.as_view(), name='course_detail'),
]
