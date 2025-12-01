from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView

from .views import to_logout

urlpatterns = [
    path('', views.ImageListView.as_view(), name='index'),
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
    path('accounts/password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

]
