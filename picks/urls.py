from django.urls import path

from .views import SignUpView, PicksView, HomeView, ThanksView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('picks/', PicksView.as_view(), name='picks'),
    path('thankyou', ThanksView.as_view(), name='thanks'),
]