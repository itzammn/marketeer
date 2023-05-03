from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    """Form definition for Profile."""

    class Meta:
        """Meta definition for Profileform."""

        model = Profile
        fields = ('pic','bio','city','dob')
