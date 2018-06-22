from django.urls import include, path

from . import views


app_name = 'accounts'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/<admin_id>/agent/signup/', views.agent_signup, name='agent_signup'),
    path('accounts/admin/signup/', views.AdminSignUpView.as_view(), name='admin_signup'),
]