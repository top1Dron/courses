import json
from catalog.models import Course
from catalog.serializers import CourseDetailSerializer, CourseListSerializer
from catalog import services
from datetime import date
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

client = Client()
factory = APIRequestFactory()


class CourseTest(TestCase):
    '''Test module for Course model'''


    def setUp(self):
        Course.objects.create(
            name='test', start_date=date(year=2021, month=2, day=3), 
            end_date=date(year=2021, month=2, day=4), lections_quantity=1
        )


    def test_course_to_str(self):
        test_course = Course.objects.get(name='test')
        self.assertEqual(str(test_course), 'test')


class GetAllCoursesTest(TestCase):
    ''' Test for GET list of all courses'''


    def setUp(self):
        Course.objects.create(
            name='Mathematics', start_date=date(year=2021 ,month=2 , day=1), 
            end_date=date(year=2021 ,month=2 , day=10), lections_quantity=3
        )
        Course.objects.create(
            name='Database', start_date=date(year=2021 ,month=1 , day=30), 
            end_date=date(year=2021 ,month=6 , day=6), lections_quantity=23
        )
        Course.objects.create(
            name='OOP', start_date=date(year=2021 ,month=1 , day=31), 
            end_date=date(year=2021 ,month=6 , day=10), lections_quantity=30
        )
        Course.objects.create(
            name='Python', start_date=date(year=2020 ,month=9 , day=1), 
            end_date=date(year=2021 ,month=6 , day=6), lections_quantity=65
        )


    def test_get_all_courses(self):
        response = client.get(reverse('catalog:courses_list'))

        request = factory.get(reverse('catalog:courses_list'))
        courses = services.get_all_cources()
        serializer = CourseListSerializer(courses, many=True, context={'request': Request(request)})
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetCourseTest(TestCase):
    ''' Test for GET course by id'''

    def setUp(self):
        self.mathematics = Course.objects.create(
            name='Mathematics', start_date=date(year=2021 ,month=2 , day=1), 
            end_date=date(year=2021 ,month=2 , day=10), lections_quantity=3
        )
        self.database = Course.objects.create(
            name='Database', start_date=date(year=2021 ,month=1 , day=30), 
            end_date=date(year=2021 ,month=6 , day=6), lections_quantity=23
        )
        self.oop = Course.objects.create(
            name='OOP', start_date=date(year=2021 ,month=1 , day=31), 
            end_date=date(year=2021 ,month=6 , day=10), lections_quantity=30
        )
        self.python = Course.objects.create(
            name='Python', start_date=date(year=2020 ,month=9 , day=1), 
            end_date=date(year=2021 ,month=6 , day=6), lections_quantity=65
        )


    def test_get_valid_course(self):
        response = client.get(
            reverse('catalog:course_detail', 
                kwargs={'id': self.python.pk}))

        course = services.get_course_by_id(self.python.pk)
        serializer = CourseDetailSerializer(course)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_invalid_course(self):
        response = client.get(
            reverse('catalog:course_detail', 
                kwargs={'id': 1000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewCourseTest(TestCase):
    ''' Test for inserting new course '''


    def setUp(self):
        self.valid_form = {
            'name': 'Database',
            'start_date': '2021-02-01',
            'end_date': '2021-03-01',
            'lections_quantity': 4
        }

        self.invalid_form = {
            'name': '',
            'start_date': '2021-02-01',
            'end_date': '2021-03-01',
            'lections_quantity': 4
        }


    def test_create_valid_course(self):
        response = client.post(
            reverse('catalog:courses_list'),
            data=json.dumps(self.valid_form),
            content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_invalid_course(self):
        response = client.post(
            reverse('catalog:courses_list'),
            data=json.dumps(self.invalid_form),
            content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        
class UpdateCourseTest(TestCase):
    ''' Test for updating information in an existing course '''

    def setUp(self):
        self.python = Course.objects.create(
            name='Python', start_date=date(year=2020 ,month=9 , day=1), 
            end_date=date(year=2021 ,month=6 , day=6), lections_quantity=65
        )
        self.valid_form = {
            'name': 'Python',
            'start_date': '2021-02-01',
            'end_date': '2021-06-06',
            'lections_quantity': 24
        }
        self.invalid_form = {
            'name': '',
            'start_date': '2021-02-01',
            'end_date': '2021-03-01',
            'lections_quantity': 4
        }


    def test_valid_update_course(self):
        response = client.put(
            reverse('catalog:course_detail', 
                kwargs={'id': self.python.pk}), 
            data=json.dumps(self.valid_form),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_invalid_update_course(self):
        response = client.put(
            reverse('catalog:course_detail', 
                kwargs={'id': self.python.pk}), 
            data=json.dumps(self.invalid_form),
            content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteCourseTest(TestCase):
    ''' Test for deleting an existing course '''

    def setup(self):
        self.python = Course.objects.create(
            name='Python', start_date=date(year=2020 ,month=9 , day=1), 
            end_date=date(year=2021 ,month=6 , day=6), lections_quantity=65
        )

    
    def test_valid_delete_course(self):
        response = client.delete(
            reverse('catalog:course_detail',
                kwargs={'id': self.python.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_valid_delete_course(self):
        response = client.delete(
            reverse('catalog:course_detail',
                kwargs={'id': 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)