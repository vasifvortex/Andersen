from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from tasks.models import Task

User = get_user_model()

class TaskAPITest(APITestCase):
    def setUp(self):
        # Create user directly
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Obtain token
        url = reverse('token_obtain_pair')
        response = self.client.post(url, {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)
        self.token = response.data['access']
     
        # Set token for future requests
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        # Create task for testing
        self.task = Task.objects.create(
            title='Test Task',
            description='Test description',
            user_id=self.user
            
              
        )

    def test_create_task(self):
        data = {'title': 'New Task', 'description': 'Test description','user_id': self.user.id}
        response = self.client.post(reverse('create-task'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_list_tasks(self):
        response = self.client.get(reverse("task-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_tasks_by_status(self):
        response = self.client.get(reverse("task-list") + "?status=new")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_tasks(self):
        response = self.client.get(reverse('user-tasks', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_task_detail(self):
        response = self.client.get(reverse('task-detail', args=[self.task.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task(self):
        data = {'title': 'Updated Task', 'status': 'in_progress','user_id': self.user.id}
        response = self.client.put(reverse('update-task', args=[self.task.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        response = self.client.delete(reverse('delete-task', args=[self.task.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_complete_task(self):
        response = self.client.patch(reverse('task-complete', args=[self.task.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_registration(self):
        self.client.credentials()  
        data = {'username': 'newuser','first_name':'new_name', 'password': 'newpassword'}
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
