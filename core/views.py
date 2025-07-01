# Create your views here.
import re
from rapidfuzz.fuzz import token_set_ratio
from django.shortcuts import render, redirect
from .models import LostItem, FoundItem
from .forms import LostItemForm, FoundItemForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, 'home.html')


def post_lost_items(request):
    if request.method == 'POST':
        form = LostItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LostItemForm()
    return render(request, 'post_lost.html', {'form':form})

def lost_items_list(request):
    lost_items = LostItem.objects.all().order_by('-date_lost')
    return render (request, 'lost_items_list.html', {'lost_items': lost_items})

def post_found_items(request):
    if request.method == 'POST':
        form = FoundItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FoundItemForm()
    return render(request, 'post_found.html',{'form':form})

def found_items_list(request):
    found_items = FoundItem.objects.all().order_by('-date_found')  # newest first
    return render(request, 'found_items_list.html', {'found_items': found_items})

#helper function for matching
def normalize(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # remove punctuation
    return text
@login_required
@user_passes_test(lambda u: u.is_staff)
def match_found_to_lost(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("🚫 This page is for employees only.")
    found_items = FoundItem.objects.all()
    matched_pairs = []

    for found in found_items:
        # Combine and normalize text for the found item
        found_text = normalize(f"{found.title} {found.description}")

        # Only compare with lost items in the same category
        lost_candidates = LostItem.objects.all()

        matches = []
        for lost in lost_candidates:
            lost_text = normalize(f"{lost.title} {lost.description}")
            score = token_set_ratio(found_text, lost_text)

            if score >= 50:  # Threshold for a "good" match
                matches.append((lost, score))

        if matches:
            matches = sorted(matches, key=lambda x: x[1], reverse=True)
            matched_pairs.append((found, matches))

    return render(request, 'match_found_to_lost.html', {'matched_pairs': matched_pairs})


@login_required
@user_passes_test(lambda u: u.is_staff)
def claim_lost_item(request, item_id):
    item = get_object_or_404(LostItem, id=item_id)
    item.claimed = True
    item.save()
    return redirect('lost_items_list')  # or wherever you want to redirect

@login_required
@user_passes_test(lambda u: u.is_staff)
def claim_found_item(request, item_id):
    item = get_object_or_404(FoundItem, id=item_id)
    if not item.claimed:
        item.claimed = True
        item.save()
    return redirect('found_items_list')
