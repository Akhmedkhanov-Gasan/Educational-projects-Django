from django.urls import path
from .views import ReviewView, ThanksView, ReviewListView, ReviewDetailView


urlpatterns = [
    path('', ReviewView.as_view()),
    path('thanks', ThanksView.as_view()),
    path('reviews', ReviewListView.as_view()),
    path('reviews/<int:pk>', ReviewDetailView.as_view()),

]
