from django.urls import path
from . import views

urlpatterns = [
    path('admin/courses/<int:course_id>/', views.delete_edit_course, name='delete_edit_course'),
    path('admin/courses/reports/', views.generate_reports, name='generate_reports'),
    path('admin/courses/', views.create_course, name='create_course'),
]