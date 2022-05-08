from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib import messages
from account.form.proxyuserforms import (
    # CompanyRegrastrationForm,
    RegistrationForm,
    CompanyForm2,
)
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class LoginViewPage(LoginView):
    template_name = "accounts/registration/login.html"
    redirect_authenticated_user = True
    next_page = reverse_lazy("root:home")


class SingUpPageView(CreateView):
    template_name = "accounts/registration/singup.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("account:log_in")

    def form_valid(self, form):
        try:
            if self.request.user.is_authenticated:
                logout(self.request)
                return reverse_lazy("account:log_in")
        except Exception as e:
            raise e

        messages.success(self.request, "account create sucess fully")
        return super().form_valid(form)


# class CopanyRegrastrationView(CreateView):
#     template_name = "accounts/registration/companylogin.html"
#     form_class = CompanyRegrastrationForm
#     success_url = reverse_lazy("account:log_in")

#     def form_valid(self, form):
#         try:
#             if self.request.user.is_authenticated:
#                 logout(self.request)
#                 return reverse_lazy("account:log_in")
#         except Exception as e:
#             raise e

#         messages.success(self.request, "account create sucess fully")

#         return super(CopanyRegrastrationView, self).form_valid(form)


class RegrastrationViewCompany(LoginRequiredMixin, CreateView):
    template_name = "accounts/registration/company2login.html"
    form_class = CompanyForm2
    success_url = reverse_lazy("root:home")

    def form_valid(self, form):
        user = self.request.user
        user.user_type.append(user.ProfileType.Company)
        user.save()
        form.instance.user = self.request.user
        return super().form_valid(form)
