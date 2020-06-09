from django.shortcuts import render, HttpResponse, reverse
from .forms import LoginForm, RegisterForm, CreatePostForm
from django.views.generic import FormView, View, TemplateView
from .models import Post
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/welcome.html'


class Login(FormView):
    form_class = LoginForm
    template_name = 'login.html'

    def form_valid(self, form):
        cd = form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password'])
        if user is not None:
            login(self.request, user)
        else:
            return super(Login, self).form_invalid(form)
        return super(Login, self).form_valid(form)

    def form_invalid(self, form):
        pass

    def get_success_url(self):
        return reverse('user:dashboard')


class Register(FormView):
    form_class = RegisterForm
    template_name = 'register.html'

    def form_valid(self, form):
        try:
            user = form
            user_new = user.save(commit=False)
            user_new.set_password(
                form.cleaned_data['password1']
            )
            user_new.save()
            return super(Register, self).form_valid(form)
        except Exception as e:
            self.form_invalid(form)

    def form_invalid(self, form):
        return render(self.request, 'register.html', {'form': form, 'error': 'Something Went Wrong'})

    def get_success_url(self):
        return reverse('user:dashboard')


class CreatePost(LoginRequiredMixin, FormView):
    form_class = CreatePostForm
    template_name = 'post.html'

    def form_valid(self, form):
        try:
            post = form
            add_post = post.save(commit=False)
            add_post.user = self.request.user
            add_post.save()
            return super(CreatePost, self).form_valid(form)
        except Exception as e:
            self.form_invalid(form)

    def form_invalid(self, form):
        return render(self.request, 'register.html', {'form': form, 'error': 'Invalid Post'})

    def get_success_url(self):
        return reverse('user:dashboard')
