from django.urls import path, reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from . import views

urlpatterns = [
    path('', views.connexion, name="connexion"),
    path('deconnexion', views.deconnexion, name="deconnexion"),
    path('registration', views.registration, name="registration"),
    # path('reset-password', PasswordResetView.as_view(), name='password_reset'),
    # path('reset-password/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset-password/confirm/<uidb64>[0-9A-Za-z]+)-<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset-password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
