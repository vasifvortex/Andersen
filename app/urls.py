from django.urls import path
from .views import TaskListAPIView,UserTaskListAPIView,TaskDetailAPIView,TaskCreateAPIView,TaskUpdateAPIView,TaskDeleteAPIView,UserRegisterAPIView,TaskFilterAPIView,TaskCompleteAPIView 
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tasks/', TaskListAPIView.as_view(), name='all-tasks'),
    path('users/<int:user_id>/tasks/', UserTaskListAPIView.as_view(), name='user-tasks'),
    path('tasks/<int:id>/', TaskDetailAPIView.as_view(), name='task-detail'),
    path('tasks/create/', TaskCreateAPIView.as_view(), name='create-task'),
    path('tasks/<int:id>/update/', TaskUpdateAPIView.as_view(), name='update-task'),
    path('tasks/<int:id>/delete/', TaskDeleteAPIView.as_view(), name='delete-task'),
    path('tasks/filter', TaskFilterAPIView.as_view(), name='task-list'),
    path('tasks/<int:id>/complete/', TaskCompleteAPIView.as_view(), name='task-complete'),
    
]

