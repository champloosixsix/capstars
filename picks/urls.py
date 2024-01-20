from django.urls import path

from .views import SignUpView, PicksView, HomeView, ThanksView, CancelView, subscription_confirm, profile, cancel

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('picks/', PicksView.as_view(), name='picks'),
    path('thankyou/', ThanksView.as_view(), name='thanks'),
    path("subscription-confirm/", subscription_confirm, name="subscription_confirm"),
    path("profile/", profile, name="profile"),
    path("cancel/", cancel, name="cancel"),
    path("cancel-confirm/", CancelView.as_view(), name='cancel_confirm'),
   
]