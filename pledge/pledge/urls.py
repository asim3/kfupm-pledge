from django.contrib import admin
from django.urls import path
from student.views import HomeView
from administration.views import StudentView

urlpatterns = [
    path('admin/student', StudentView.as_view()),
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
]
