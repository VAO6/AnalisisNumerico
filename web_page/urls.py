from django.urls import path

from . import views

urlpatterns = [
    path("", views.web_page_index, name="web_page_index"),
    path("<int:pk>/", views.web_page_detail, name="web_page_detail"),
]