from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render, get_object_or_404

from .forms import AdminSignUpForm, AgentSignupForm, CreateAgentForm
from .models import Admin, Agent

# Create your views here.


class AdminSignUpView(generic.CreateView):
    form_class = AdminSignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('accounts:login')


def agent_signup(request, admin_id):
    admin = get_object_or_404(Admin, pk=admin_id)

    if request.method == 'POST':
        form = AgentSignupForm(request.POST)

        if form.is_valid():
            new_agent = form.save(commit=False)
            new_agent.set_password(form.cleaned_data["password1"])
            new_agent.is_agent = True
            new_agent.save()
            Agent.objects.create(user=new_agent, admin=admin)
            phone_number = form.cleaned_data.get('phone_number')
            password = form.cleaned_data.get('password1')
            user = authenticate(phone_number=phone_number, password=password)
            login(request, user)
            return redirect('accounts:login')

    else:
        form = AgentSignupForm()
    return render(request, 'registration/signup.html', {'form': form})


def send_message(request, admin_id):
    """
    This is the function that will receive the agent phone number as a form POST and implements the
    sending of the text message to the user. The text message is a url where the agent can create
    their account. The url link will be different for each admin user.
    :return:
    """
    if request.method == 'POST':
        agent_number = request.POST.get('agent_phone_number')
        # The logic for sending the message will be here.
    form = CreateAgentForm()
    return render(request, 'registration/create_agent.html', {'form': form})
