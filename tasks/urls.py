from django.urls import path,re_path
from .views import TaskListAPIView,UserTaskListAPIView,TaskDetailAPIView,TaskCreateAPIView,TaskUpdateAPIView,TaskDeleteAPIView,UserRegisterAPIView,TaskCompleteAPIView 
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Andersen API",
      default_version='v1',
      description="API documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="vasif.oruczade@gmail.com"),
      license=openapi.License(name="This project is licensed by Vasif Orujzade."),
   ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)
swagger_settings = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
        }
    }
}

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tasks/', TaskListAPIView.as_view(), name='task-list'),
    path('users/<int:user_id>/tasks/', UserTaskListAPIView.as_view(), name='user-tasks'),
    path('tasks/<int:id>/', TaskDetailAPIView.as_view(), name='task-detail'),
    path('tasks/create/', TaskCreateAPIView.as_view(), name='create-task'),
    path('tasks/<int:id>/update/', TaskUpdateAPIView.as_view(), name='update-task'),
    path('tasks/<int:id>/delete/', TaskDeleteAPIView.as_view(), name='delete-task'),
    path('tasks/<int:id>/complete/', TaskCompleteAPIView.as_view(), name='task-complete'),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]

