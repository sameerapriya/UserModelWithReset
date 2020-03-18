from django.urls import path,include
from .views import registration_view,login_view, view_profile,change_password
from django.conf.urls import url
from django.contrib.auth.views import LoginView,PasswordResetView,PasswordResetConfirmView,PasswordResetCompleteView,PasswordResetDoneView

app_name = 'api'

urlpatterns =[
    path('users/',registration_view),
    path('login/',LoginView.as_view(template_name='api/login.html',redirect_field_name='api/profile')),
    url(r'^profile/$',view_profile),
    url(r'^profile/(?P<pk>\d+)/$',view_profile),
    url(r'^change-password/$',change_password),
    url(r'^reset-password/$',PasswordResetView.as_view(template_name='api/password_reset_form.html')),
    url(r'^reset-password/done/$',PasswordResetDoneView.as_view(template_name='api/password_reset_done.html')),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',PasswordResetConfirmView.as_view(template_name='api/password_reset_confirm.html')),
    url(r'^password/complete/$',PasswordResetCompleteView.as_view(template_name='api/password_reset_confirm.html')),

]
