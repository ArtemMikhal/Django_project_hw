import string
import random

from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View

from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User



class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


    def form_valid(self, form):
        response = super().form_valid(form)
        new_user = form.save()
        # Создаем и сохраняем токен подтверждения
        token = ''.join(random.choices(string.ascii_letters + string.digits, k=50))
        new_user.email_verification_token = token
        new_user.save()
        # Отправляем письмо с подтверждением
        current_site = get_current_site(self.request)
        mail_subject = 'Подтвердите ваш аккаунт'
        message = (
            f'Поздравляем, Вы зарегистрировались на нашем портале!\n'
            f'Для завершения регистрации и подтверждения вашей электронной почты, '
            f'пожалуйста, кликните по следующей ссылке:\n'
            f'http://{current_site.domain}{reverse("users:verify_email", kwargs={"uid": new_user.pk, "token": token})}'
        )
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email])
        return super().form_valid(form)

class VerifyEmailView(View):
    def get(self, request, uid, token):
        try:
            user = User.objects.get(pk=uid, email_verification_token=token)
            user.is_active = True
            user.save()
            return render(request, 'users/registration_success.html')  # Покажем сообщение о регистрации
        except User.DoesNotExist:
            return render(request, 'users/registration_failed.html')  # Покажем сообщение об ошибке

class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

