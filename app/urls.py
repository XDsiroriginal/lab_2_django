from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeView

from .views import to_logout, first_name_change, last_name_change, email_change
from .views import to_profile
from .views import change_user_avatar
from .views import register_view
from .views import login_change

urlpatterns = [
    path('accounts/image-list', views.ImageListView.as_view(), name='image-list'),
]

urlpatterns += [
    path('', views.index, name='index'),
]

urlpatterns += [
    path(r'^image/(?P<pk>\d+)$', views.ImageDetailView.as_view(), name='image-detail'),
]

urlpatterns += [
    path('accounts/login/', LoginView.as_view(next_page='index'), name='login'),
]

urlpatterns += [
    path('accounts/to_logout/', to_logout, name='to_logout'),
    path('accounts/logout/', LogoutView.as_view(next_page='index'), name='logout'),
]

urlpatterns += [
    path('accounts/password_change/', PasswordChangeView.as_view(success_url=reverse_lazy('profile')), name='password_change'),
]

urlpatterns += [
    path('profile', to_profile, name='profile'),
]

urlpatterns += [
    path('image/<int:pk>/change_user_avatar/', change_user_avatar, name='change_user_avatar'),
]

urlpatterns += [
    path('accounts/register', register_view, name='register'),
]

urlpatterns += [
    path('accounts/change_login/', login_change, name='login_change'),
    path('accounts/change_first_name/', first_name_change, name='first_name_change'),
    path('accounts/change_last_name/', last_name_change, name='last_name_change'),
    path('accounts/change_email/', email_change, name='email_change'),
]