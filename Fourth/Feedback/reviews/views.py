from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView

from .forms import ReviewForm
from .models import Review

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, 'reviews/review.html', {'form': form})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks')
        return render(request, 'reviews/review.html', {'form': form})

class ThanksView(TemplateView):
    template_name = 'reviews/thanks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Fuck you!! again'
        return context

class ReviewListView(TemplateView):
    template_name = 'reviews/review_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context['reviews'] = reviews
        return context

class ReviewDetailView(TemplateView):
    template_name = 'reviews/review_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        selected_review = Review.objects.get(pk=review_id)
        context['review'] = selected_review
        return context
