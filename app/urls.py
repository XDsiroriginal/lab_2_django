from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeView

urlpatterns = [
    path('accounts/image-list', views.ImageListView.as_view(), name='image-list'),
    path('image/<int:pk>', views.ImageDetailView.as_view(), name='image-detail'),

    path('profile', views.to_profile, name='profile'),
    path('profile/<str:status>/', views.to_profile, name='profile_filtered'),

    path('profile/admin', views.admin_profile_view, name='admin_profile'),
    path('', views.index, name='index'),  # Добавим сюда index

    path('accounts/register', views.register_view, name='register'),
    path('accounts/login/', LoginView.as_view(next_page='index'), name='login'),
    path('accounts/to_logout/', views.to_logout, name='to_logout'),
    path('accounts/logout/', LogoutView.as_view(next_page='index'), name='logout'),

    path('accounts/change_login/', views.login_change, name='login_change'),
    path('accounts/change_first_name/', views.first_name_change, name='first_name_change'),
    path('accounts/change_last_name/', views.last_name_change, name='last_name_change'),
    path('accounts/change_email/', views.email_change, name='email_change'),
    path('accounts/change_patronymic/', views.patronymic_change, name='patronymic_change'),
    path('accounts/password_change/', PasswordChangeView.as_view(success_url=reverse_lazy('profile')),
         name='password_change'),
    path('image/<int:pk>/change_user_avatar/', views.change_user_avatar, name='change_user_avatar'),

    path('profile/create_new_application', views.create_new_application, name='create_new_application'),
    path('profile/application/<int:pk>', views.ApplicationDetailView.as_view(), name='application-detail'),
    path('profile/application/<int:pk>/delete', views.application_delete, name='application_delete'),
    path('profile/application/<int:pk>/change/', views.application_change, name='application_change'),
    path('profile/application/<int:pk>/delete/comfirm', views.application_delete_comfirm,
         name='application_delete_comfirm'),

    path('profile/admin/categories/', views.categories_change_view, name='categories_change'),
    path('profile/admin/categories/create_new_category', views.create_new_application, name='create_new_application'),
    path('app/profile/admin/categories/change/<int:pk>/', views.categories_delete_change, name='categories_delete_change'),
    path('app/profile/admin/categories/change/<int:pk>/delete_comfirm/', views.categories_delete_confirm, name='categories_delete_confirm'),
    path('app/profile/admin/categories/change/<int:pk>/delete/', views.category_delete, name='category_delete'),
]
