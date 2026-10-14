from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("favicon.ico", RedirectView.as_view(url="/static/market/favicon.svg", permanent=True)),
    path("favicon.png", RedirectView.as_view(url="/static/market/favicon.svg", permanent=True)),
    path("", include("market.urls")),
]
