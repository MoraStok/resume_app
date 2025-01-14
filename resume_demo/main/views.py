from django.shortcuts import render
from django.contrib import messages
from .models import (
		UserProfile,
		Certificate
	)
from django.views import generic
from . forms import ContactForm

class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		certificates = Certificate.objects.filter(is_active=True)
		
		context["certificates"] = certificates
		return context


class ContactView(generic.FormView):
	template_name = "main/contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)
	
class CertificateView(generic.ListView):
	model = Certificate
	template_name = "main/certificates.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)
	
class CertificateDetailView(generic.DetailView):
	model = Certificate
	template_name = "main/certificate_detail.html"
