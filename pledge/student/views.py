from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from .forms import PledgeForm
from django.contrib.messages.views import SuccessMessageMixin


class HomeView(TemplateView):
    template_name = "student/home.html"


class PledgeView(SuccessMessageMixin, FormView):
    template_name = "student/pledge.html"
    form_class = PledgeForm
    success_url = reverse_lazy("home")
    success_message = "was created successfully"
