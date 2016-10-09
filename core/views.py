from registration.backends.hmac.views import RegistrationView

from .forms import CustomRegistrationForm


class CustomRegistrationView(RegistrationView):
    form_class = CustomRegistrationForm
