from django.urls import path
from .views import (
    ReviewView,
    ThanksView,
    ReviewListView,
    ReviewDetailView,
    AddFavoriteView
)


urlpatterns = [
    path('', ReviewView.as_view()),
    path('thanks', ThanksView.as_view()),
    path('reviews', ReviewListView.as_view()),
    path('reviews/favorite', AddFavoriteView.as_view()),
    path('reviews/<int:pk>', ReviewDetailView.as_view()),
]
