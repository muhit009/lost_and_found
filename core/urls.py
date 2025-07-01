from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post-lost/', views.post_lost_items, name='post_lost'),
    path('lost-items/', views.lost_items_list, name='lost_items_list'),
    path('post-found/', views.post_found_items, name='post_found'),
    path('found-items/', views.found_items_list, name='found_items_list'),
    path('match-found-to-lost/', views.match_found_to_lost, name='match_found_to_lost'),
    path('claim-lost/<int:item_id>/', views.claim_lost_item, name='claim_lost_item'),
    path('claim-found/<int:item_id>/', views.claim_found_item, name='claim_found_item'),

]