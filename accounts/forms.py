from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Admin, Agent


class AdminSignUpForm(UserCreationForm):
    business_name = forms.CharField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ('phone_number', 'fullname', 'business_name', 'password1', 'password2',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_admin = True

        if commit:
            user.save()
            Admin.objects.create(user=user, business_name=self.cleaned_data.get('business_name'))
            user.save()
        return user


class AgentSignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('phone_number', 'fullname', 'password1', 'password2')
    # I could have override the save method of here, but that will cause a difficulty when trying to
    # implement an agent signup view function that will receive an instance of the associated admin
    # instance.


class CreateAgentForm(forms.Form):
    agent_phone_number = forms.CharField(max_length=12)
