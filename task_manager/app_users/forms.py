from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy

from task_manager.app_users.models import ApplicationUser

MAX_LENGTH = 100


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=MAX_LENGTH,
        label=(gettext_lazy('Name')),
        required=True,
    )
    last_name = forms.CharField(
        max_length=MAX_LENGTH,
        label=(gettext_lazy('Last Name')),
        required=True,
    )

    class Meta:
        model = ApplicationUser
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
        ]
