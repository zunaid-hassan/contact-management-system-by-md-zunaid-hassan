from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("contacts.urls")),
]

# contacts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.contact_list, name="contact_list"),
    path("contact/<int:pk>/", views.contact_detail, name="contact_detail"),
    path("contact/new/", views.contact_create, name="contact_create"),
    path("contact/<int:pk>/edit/", views.contact_update, name="contact_update"),
    path("contact/<int:pk>/delete/", views.contact_delete, name="contact_delete"),
]
