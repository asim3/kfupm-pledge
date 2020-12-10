from django.contrib import admin
from django.urls import path
from student.views import HomeView, PledgeView, LoginView
from administration.views import StudentView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('pledge/', PledgeView.as_view()),
    path('admin/student/', StudentView.as_view()),
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
]
