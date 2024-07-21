from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from loginapp.models import Course, Program
from loginapp.serializers import ProgramSerializer, CourseSerializer
from rest_framework.authtoken.models import Token


class UserRegisterViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register')  # Adjust URL pattern name if necessary
        self.user_register_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword',
            'first_name': 'Test',
            'last_name': 'User'
        }
        self.user_register = User.objects.create_user(**self.user_register_data)

    def test_user_registration(self):
        response = self.client.post(self.register_url, self.user_register_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)
        self.assertEqual(User.objects.count(), 1)


class CourseViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.course_url = reverse('course-list')  # Adjust URL pattern name if necessary
        self.course_data = {
            'name': 'Test Course',
        }
        self.course = Course.objects.create(**self.course_data)

        # Create and authenticate a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_course_list(self):
        response = self.client.get(self.course_url)
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_course(self):
        response = self.client.post(self.course_url, self.course_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 2)

    def test_update_course(self):
        update_data = {
            'name': 'Updated Course'
        }
        url = reverse('course-detail', args=[self.course.id])
        response = self.client.patch(url, update_data, format='json')
        self.course.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.course.name, 'Updated Course')

    def test_delete_course(self):
        url = reverse('course-detail', args=[self.course.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.count(), 0)


class ProgramViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.program_url = reverse('program-list')  # Adjust URL pattern name if necessary
        self.program_data = {
            'name': 'Test Program',
        }
        self.program = Program.objects.create(**self.program_data)

        # Create and authenticate a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_program_list(self):
        response = self.client.get(self.program_url)
        programs = Program.objects.all()
        serializer = ProgramSerializer(programs, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_program(self):
        response = self.client.post(self.program_url, self.program_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Program.objects.count(), 2)

    def test_update_program(self):
        update_data = {
            'name': 'Updated Program'
        }
        url = reverse('program-detail', args=[self.program.id])
        response = self.client.patch(url, update_data, format='json')
        self.program.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.program.name, 'Updated Program')

    def test_delete_program(self):
        url = reverse('program-detail', args=[self.program.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Program.objects.count(), 0)
