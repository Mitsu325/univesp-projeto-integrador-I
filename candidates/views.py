from django.views.generic import TemplateView


class HomeCandidates(TemplateView):
    template_name = "home_candidates.html"

class RegisterCandidates(TemplateView):
    template_name = "register_candidates.html"
