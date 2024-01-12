from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Picks
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from .forms import CustomUserCreationForm

class HomeView(TemplateView):
    template_name = 'home.html'

    def post(self, request):
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            #enter what you want the form to do
            
            from_email = "capstars@capstarsinc.com"
            message = '''
            Name:\t{}\n
            Subject:\t{}\n
            Email:\t{}\n
            Message:\t{}\n
            '''.format(name, subject, email, message)
            try:
                send_mail(subject, message, from_email, ["capstars@capstarsinc.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return HttpResponseRedirect('/picks/thankyou')
        return render(request, '/picks/thankyou')
    
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class PicksView(LoginRequiredMixin, ListView):
    login_url='login'
    redirect_field_name='redirect_to'
    template_name = 'picks.html'
    model = Picks

    def get_queryset(self, *args, **kwargs):
        qs = Picks.objects.all()
        qs = qs.filter(closed=False)
        return qs

class ThanksView(TemplateView):
    template_name = 'thankyou.html'
