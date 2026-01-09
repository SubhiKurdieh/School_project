from django.urls import path, include

urlpatterns = [
    path('api/', include('students.urls')),
    path('api/', include('finance.urls')),
    path('api/', include('teacher.urls')),
    path('api/', include('admin_panel.urls')),
]