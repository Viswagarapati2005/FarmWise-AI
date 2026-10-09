from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json

from .models import District, Crop, CropReview, PestAlert, ForumPost, Notification
from .data import AP_DISTRICTS, CROPS_DATA, REVIEWS_DATA, PESTS_DATA, FORUM_DATA, ALERTS_DATA, YIELD_DATA


def dashboard(request):
    # Use hardcoded data (no DB required for demo)
    context = {
        'screen': 'dashboard',
        'total_reviews': 18342,
        'active_farmers': 12489,
        'avg_yield_rating': 4.2,
        'pest_reports': 63,
        'top_crops': CROPS_DATA[:6],
        'recent_reviews': REVIEWS_DATA[:3],
        'alert_text': 'Brown Planthopper outbreak in Krishna & Guntur — 4,100 acres · IMD Orange Alert: Heavy rain East Godavari Thu–Sat · MSP for Paddy raised to ₹2,300/quintal',
    }
    return render(request, 'core/dashboard.html', context)


def reviews(request):
    season_filter = request.GET.get('season', '')
    district_filter = request.GET.get('district', '')
    filtered = REVIEWS_DATA
    if season_filter:
        filtered = [r for r in filtered if r.get('season','').lower() == season_filter.lower()]
    context = {
        'screen': 'reviews',
        'reviews': filtered,
        'seasons': ['Kharif','Rabi','Summer'],
        'season_filter': season_filter,
    }
    return render(request, 'core/reviews.html', context)


def regions(request):
    context = {
        'screen': 'regions',
        'districts': AP_DISTRICTS,
        'districts_json': json.dumps(AP_DISTRICTS),
    }
    return render(request, 'core/regions.html', context)


def water_climate(request):
    context = {
        'screen': 'water',
        'crops': CROPS_DATA,
    }
    return render(request, 'core/water_climate.html', context)


def pest_tracker(request):
    context = {
        'screen': 'pest',
        'pests': PESTS_DATA,
    }
    return render(request, 'core/pest_tracker.html', context)


def yield_profit(request):
    context = {
        'screen': 'yield',
        'yield_data': YIELD_DATA,
    }
    return render(request, 'core/yield_profit.html', context)


def forum(request):
    topic_filter = request.GET.get('topic', '')
    filtered = FORUM_DATA
    if topic_filter:
        filtered = [f for f in filtered if f.get('topic','').lower() == topic_filter.lower()]
    context = {
        'screen': 'forum',
        'posts': filtered,
        'topics': ['Rice','Cotton','Irrigation','Pest Control','Weather'],
        'topic_filter': topic_filter,
    }
    return render(request, 'core/forum.html', context)


def upload(request):
    context = {'screen': 'upload'}
    return render(request, 'core/upload.html', context)


def alerts(request):
    unread_count = sum(1 for a in ALERTS_DATA if a.get('unread'))
    context = {
        'screen': 'alerts',
        'alerts': ALERTS_DATA,
        'unread_count': unread_count,
    }
    return render(request, 'core/alerts.html', context)


def district_detail(request, district_name):
    district = next((d for d in AP_DISTRICTS if d['name'] == district_name), None)
    if not district:
        return JsonResponse({'error': 'Not found'}, status=404)
    return JsonResponse(district)


@require_POST
def upvote_review(request, review_id):
    return JsonResponse({'success': True, 'new_count': review_id + 142})
