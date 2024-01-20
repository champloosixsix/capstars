from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from .models import Picks
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import get_user_model
import stripe
import djstripe
from djstripe.settings import djstripe_settings
from djstripe.models import Subscription
from .forms import CustomUserCreationForm
from django.conf import settings
stripe.api_key = settings.STRIPE_TEST_SECRET_KEY



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

@login_required
def subscription_confirm(request):
    # set our stripe keys up
    stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY

    # get the session id from the URL and retrieve the session object from Stripe
    session_id = request.GET.get("session_id")
    session = stripe.checkout.Session.retrieve(session_id)

    # get the subscribing user from the client_reference_id we passed in above
    client_reference_id = int(session.client_reference_id)
    subscription_holder = get_user_model().objects.get(id=client_reference_id)
    # sanity check that the logged in user is the one being updated
    assert subscription_holder == request.user

    # get the subscription object form Stripe and sync to djstripe
    subscription = stripe.Subscription.retrieve(session.subscription)
    djstripe_subscription = Subscription.sync_from_stripe_data(subscription)

    # set the subscription and customer on our user
    subscription_holder.subscription = djstripe_subscription
    subscription_holder.customer = djstripe_subscription.customer
    subscription_holder.save()

    # show a message to the user and redirect
    messages.success(request, f"You've successfully signed up. Thanks for the support!")
    return HttpResponseRedirect(reverse("profile"))

def profile(request):
    if request.user.is_authenticated:
        return render(request = request, template_name="profile.html" )
    else:
        return redirect("login")

    
def cancel(request):
  if request.user.is_authenticated:
    sub_id = request.user.subscription.id
    stripe.Subscription.delete(sub_id)

  return redirect("cancel_confirm")


class CancelView(TemplateView):
    template_name = 'cancel-confirm.html'

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