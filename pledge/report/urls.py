from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import ReportsView, PrintReportsView, ReasonsReportsView


urlpatterns = (
    path('reports/', ReportsView.as_view(), name='reports'),
    path('reports/<int:tearm>/', ReasonsReportsView.as_view(),
         name='reasons-reports'),
    path('reports/<int:tearm>/<slug:reasons>/',
         PrintReportsView.as_view(), name='print-reports'),
)
