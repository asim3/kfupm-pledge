from django.contrib import admin
from django.urls import path, reverse_lazy
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.views import LogoutView

from administration.views import DownloadExcelView
from student.views import HomeView, PledgeView, LoginForAllView, ReportsView


admin.site.site_header = _("Readmission Pledge Forms")
admin.site.site_title = _("Admission")
admin.site.index_title = _(
    "You can add new students using an excel file by clicking on the add student link.")
# admin.site.empty_value_display = _("empty")


urlpatterns = i18n_patterns(
    path('login/', LoginForAllView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
    path('excel/', DownloadExcelView.as_view(), name='excel'),
    path('reports/', ReportsView.as_view(), name='reports'),
    path('pledge/', PledgeView.as_view(), name='pledge'),
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
)

# Return a URL pattern for serving files in debug mode only.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
