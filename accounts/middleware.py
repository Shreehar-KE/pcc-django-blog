from django.shortcuts import redirect
from django.urls import reverse


class RedirectIfAuthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.path in [reverse('accounts:login'), reverse('accounts:register')]:
                # Assuming 'home' is the name of your home URL pattern
                return redirect('blogs:index')
        response = self.get_response(request)
        return response


class RedirectIfNotAuthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            if request.path == reverse('accounts:logout'):
                return redirect('blogs:index')  # Redirect to the login page
        response = self.get_response(request)
        return response
