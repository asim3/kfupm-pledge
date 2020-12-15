from django.contrib import admin
from django.urls import path, reverse_lazy
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.views import LoginView, LogoutView
from student.views import HomeView, PledgeView


urlpatterns = i18n_patterns(
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
    path('pledge/', PledgeView.as_view(), name='pledge'),
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
)

# Return a URL pattern for serving files in debug mode only.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
