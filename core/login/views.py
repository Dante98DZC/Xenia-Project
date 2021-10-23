from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView

class LoginFormView(LoginView):
    template_name = 'login.html'    

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Xenia | Inicio de sesión"
        return context