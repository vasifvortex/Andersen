
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
from .models import Task,User
from .serializers import TaskSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

#Get a list of all tasks; 
class TaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


#Get a list of all user's tasks; 
class UserTaskListAPIView(ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Task.objects.filter(user_id=user_id)
    

#Get information about a specific task; 
class TaskDetailAPIView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'


#Create a new task; 
class TaskCreateAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

#Update task information (can be updated only by owner); 
class TaskUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Task.objects.filter(user_id=self.request.user)
    

#Delete a task (can be deleted only by the owner).
class TaskDeleteAPIView(DestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Task.objects.filter(user_id=self.request.user)
    
#registering new users
class UserRegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# Task list with optional filtering by status
class TaskFilterAPIView(ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Task.objects.all()
        status_param = self.request.query_params.get('status')
        if status_param is not None:
            queryset = queryset.filter(status=status_param)
        return queryset

# Mark task as completed by updating the status field
class TaskCompleteAPIView(RetrieveUpdateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Task.objects.filter(user_id=self.request.user)
    
    def update(self, request, *args, **kwargs):
        task = self.get_object()
        # Force status to 'completed' regardless of request data
        task.status = Task.Status.COMPLETED
        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

 

    