from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('app/', include('app.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/app/', permanent=True)),
]
