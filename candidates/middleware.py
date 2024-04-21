from django.shortcuts import redirect
from django.urls import reverse


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path in [
            reverse("resumes:index"),
            reverse("resumes:edit"),
            reverse("resumes:config"),
        ]:
            if "manager_id" in request.session:
                return redirect("management:index")
            if "candidate_id" not in request.session:
                return redirect("candidates:index")

        if request.path in [
            reverse("candidates:index"),
            reverse("candidates:register"),
        ]:
            if "candidate_id" in request.session:
                return redirect("resumes:index")
            if "manager_id" in request.session:
                return redirect("management:index")

        if request.path == "/":
            if "candidate_id" in request.session:
                return redirect("resumes:index")
            elif "manager_id" in request.session:
                return redirect("management:index")
            else:
                return redirect("candidates:index")

        response = self.get_response(request)
        return response
