from django import forms
from django.contrib.auth.models import User
from django.db import transaction

from registration.forms import RegistrationForm


class CustomRegistrationForm(RegistrationForm):
    location = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'location', 'password1', 'password2')

    def save(self, commit=True):
        with transaction.atomic():
            user = super(CustomRegistrationForm, self).save()
            user.refresh_from_db()  # very important! this will load the profile instance created by the signal
            user.profile.location = self.cleaned_data.get('location')
            # set here all other values
            user.save()
            return user
