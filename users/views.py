from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from users.forms import UserCreateForm, UserUpdateForm


class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm()
        context = {"form": create_form}
        return render(request, "users/register.html", context)

    def post(self, request):
        create_form = UserCreateForm(data=request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect("landing_page")
        else:
            context = {
                "form": create_form
            }
            return render(request, "users/register.html", context)


class LoginView(View):
    def get(self, request):
        user_login = AuthenticationForm()
        context = {
            "user_login": user_login
        }
        return render(request, "users/login.html", context)

    def post(self, request):
        user_login = AuthenticationForm(data=request.POST)
        if user_login.is_valid():
            user = user_login.get_user()
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect("books:list")
        else:
            context = {"user_login": user_login}
            return render(request, "users/login.html", context)


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        # if not request.CustomUser.is_authenticated:   LoginRequiredMixin
        #    return redirect("CustomUsers:login")      LoginRequiredMixin
        context = {"user": request.user}
        return render(request, 'users/profile.html', context)


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, "You have successfully logged out!")
        return redirect("landing_page")


class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        user_form = UserUpdateForm(instance=request.user)
        context = {"form": user_form}
        return render(request, "users/profile_edit.html", context)

    def post(self, request):
        user_form = UserUpdateForm(instance=request.user, data=request.POST, files=request.FILES)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "You have successfully updated your profile.")
            return redirect("users:profile")

        return redirect(request, "users/profile_edit.html", {"form": user_form})
