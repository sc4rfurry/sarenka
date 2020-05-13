
from django.urls import path
from searcher.views import CVESearchView

urlpatterns = [
    path('cve/<str:code>', CVESearchView.as_view(), name="get_by_cve"),
]