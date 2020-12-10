from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "student/home.html"


class PledgeView(TemplateView):
    template_name = "student/pledge.html"


class LoginView(TemplateView):
    template_name = "student/login.html"
