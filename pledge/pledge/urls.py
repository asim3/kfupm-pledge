from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from student.views import HomeView, PledgeView
from administration.views import StudentsView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('pledge/', PledgeView.as_view(), name='pledge'),
    path('admin/student/', StudentsView.as_view(), name='admin-student'),
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
]
