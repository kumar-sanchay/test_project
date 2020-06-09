from django.db import models
from products.manager import Active, Inactive
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Custom UserModel can be used too
# class UserManager(BaseUserManager):
#     '''
#     Manager for Custom User Model.
#     '''
#     use_in_migrations = True
#
#     def _create_user(self, username, password, **extra_fields):
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, username, password, **extra_fields):
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(username=username, password=password, **extra_fields)
#
#     def create_superuser(self, username, password, **extra_fields):
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_staff', True)
#
#         if extra_fields.get('is_superuser') is False:
#             raise ValueError('Super must be set to true.')
#         return self._create_user(username=username, password=password, **extra_fields)
#
#
# class User(AbstractBaseUser):
#     '''
#     Custom User Model
#     '''
#     username = models.CharField(max_length=25, unique=True)
#     email = models.EmailField(unique=True, null=True)
#     first_name = models.CharField(max_length=25)
#     last_name = models.CharField(max_length=25, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now=True)
#     updated = models.DateTimeField(auto_now_add=True)
#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['first_name']
#     objects = UserManager()
#
#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'
#         app_label = 'user'
#
#     def has_perm(self, perm, obj=None):
#         if self.is_superuser or self.is_staff:
#             return True
#         return False
#
#     def has_module_perms(self, app_label):
#         if self.is_superuser or self.is_staff:
#             return True
#         return False


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    active_obj = Active()
    inactive_obj = Inactive()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']
        app_label = 'user'

    def __str__(self):
        return '{}::{}'.format(self.user, self.pk)