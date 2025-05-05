from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.shortcuts import render

monthly_challenges = {
    'january': 'Firs month',
    'february': 'Secondary month',
    'march': 'Third month',
    'april': 'Fourth month',
    'may': 'Fifth month',
    'june': 'Sixth month',
    'july': 'Seventh month',
    'august': 'Eight month',
    'september': 'Ninth month',
    'october': 'Tenth month',
    'november': 'Eleventh month',
    'december': None,
}
def index(request):
    months = list(monthly_challenges.keys())

    return render(request, 'challenges/index.html', {
        'months': months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('WTF???')

    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            'text': challenge_text,
            'month': month,
        })
    except:
        raise Http404()
