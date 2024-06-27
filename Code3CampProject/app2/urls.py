from django.urls import path
from .views import course_list, course_create, course_update, course_delete

urlpatterns = [
    path('courses/', course_list, name='course_list'),
    path('courses/new/', course_create, name='course_create'),
    path('courses/<int:pk>/edit/', course_update, name='course_update'),
    path('courses/<int:pk>/delete/', course_delete, name='course_delete'),
]
