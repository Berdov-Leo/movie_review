from django.urls import path
from reviews import views


urlpatterns = [
    path('', views.review_view, name='review'),
]
