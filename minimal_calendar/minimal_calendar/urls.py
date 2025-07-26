from django.urls import path
from tasks.views import get_tasks, create_task, update_task, register_user, login_user
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/tasks/', get_tasks),
    path('api/tasks/create/', create_task),
    path('api/tasks/<int:task_id>/update/', update_task),
    path('api/token/', obtain_auth_token),
    path('register/', register_user),
    path('token-auth/', obtain_auth_token),
    path('login/', login_user),

]
