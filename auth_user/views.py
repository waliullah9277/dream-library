from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth import login,logout,update_session_auth_hash
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from books.models import BuyBook, BorrowedBook
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.

# Email send funciton start here.
def send_authenticate_email(user, subject, template):
    message = render_to_string(template,{
        'user': user,
    })
    to_email = user.email
    send_email = EmailMultiAlternatives(subject, ' ', to=[to_email])
    send_email.attach_alternative(message, 'text/html')
    send_email.send()

#email send end.

class UserRegisterView(FormView):
    template_name = 'auth_user/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        our_user = form.save()
        messages.success(self.request, f'Your Account has been registered Successfully !')
        login(self.request, our_user)
        send_authenticate_email(self.request.user, 'Registration Complete', 'auth_user/user_registration_send_email.html')
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name = 'auth_user/user_login.html'
    def get_success_url(self):
        messages.success(self.request, f'Your Account has been Logged in Successfully !')
        return reverse_lazy('profile')
    
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, 'Your Account has been Logged out Successfully !')
        return super().dispatch(request, *args, **kwargs)
    

class UserProfileView(LoginRequiredMixin, View):
    template_name = 'auth_user/profile.html'

    def get(self,request):
        orders = BorrowedBook.objects.filter(user=request.user, returend=False)
        return render(request, self.template_name, {'orders': orders})

    
class UserUpdateView1(LoginRequiredMixin, View):
    template_name = 'auth_user/update_profile.html'

    def get(self,request):
        form = UserUpdateForm(instance = request.user)
        return render(request, self.template_name, {'form': form})
    
    def post(self,request):
        form = UserUpdateForm(request.POST, instance =request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Account information has been updated Successfully.')
            send_authenticate_email(self.request.user, 'Profile Updated', 'auth_user/user_profile_update_send_email.html')
            return redirect('profile')
        return render(request, self.template_name, {'form':form})


class UserPasswordChangeView(LoginRequiredMixin, View):
    template_name = 'auth_user/pass_change.html'

    def get(self,request, *args, **kwargs):
        form = PasswordChangeForm(request.user)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user, data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your password has been changed successfully !')
            send_authenticate_email(self.request.user, 'Password Changes', 'auth_user/user_password_change_send_email.html')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, self.template_name, {'form': form})
