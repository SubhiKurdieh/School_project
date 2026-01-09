from django.urls import path
from .views import (
    ParentStudentsView,
    StudentDashboardView,
    StudentGradesView,
)

urlpatterns = [
    path('parent/students/', ParentStudentsView.as_view()),
    path('student/<int:id>/dashboard/', StudentDashboardView.as_view()),
    path('student/<int:id>/grades/', StudentGradesView.as_view()),
]