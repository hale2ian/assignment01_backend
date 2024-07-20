from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from loginapp.models import UserRegister, Course, Program
from loginapp.serializers import UserRegisterSerializer, CourseSerializer, ProgramSerializer

class UserRegisterViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_register_url = reverse('userregister-list')
        self.user_register_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        }
        self.user_register = UserRegister.objects.create(**self.user_register_data)

    def test_get_user_register_list(self):
        response = self.client.get(self.user_register_url)
        user_registers = UserRegister.objects.all()
        serializer = UserRegisterSerializer(user_registers, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_user_register(self):
        response = self.client.post(self.user_register_url, self.user_register_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserRegister.objects.count(), 2)

    def test_update_user_register(self):
        update_data = {
            'first_name': 'Updated',
            'last_name': 'User'
        }
        url = reverse('userregister-detail', args=[self.user_register.id])
        response = self.client.patch(url, update_data, format='json')
        self.user_register.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.user_register.first_name, 'Updated')

    def test_delete_user_register(self):
        url = reverse('userregister-detail', args=[self.user_register.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(UserRegister.objects.count(), 0)

class CourseViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.course_url = reverse('course-list')
        self.course_data = {
            'name': 'Test Course',
        }
        self.course = Course.objects.create(**self.course_data)

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
        self.program_url = reverse('program-list')
        self.program_data = {
            'name': 'Test Program',
        }
        self.program = Program.objects.create(**self.program_data)

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
