from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.crypto import get_random_string
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
        token = get_random_string(length=50)
        new_user.verification_token = token
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
            recipient_list=[new_user.email]
        )
        return response


class VerifyEmailView(View):
    def get(self, request, uid, token):
        try:
            user = get_object_or_404(User, pk=uid, verification_token=token)
            user.is_verified = True
            user.save()
            return render(request, 'users/registration_success.html')  # Покажем сообщение о регистрации
        except User.DoesNotExist:
            return render(request, 'users/registration_failed.html')  # Покажем сообщение об ошибке

class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_verified:
            return HttpResponseForbidden("Ваша электронная почта еще не проверена.")
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user