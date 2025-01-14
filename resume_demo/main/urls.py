from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
	path('', views.IndexView.as_view(), name="home"),
	path('contact/', views.ContactView.as_view(), name="contact"),
    path('certificates/', views.CertificateView.as_view(), name="certificates"),
    path('certificates/<slug:slug>', views.CertificateDetailView.as_view(), name="certificate"),
]