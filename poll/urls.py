from django.urls import path
from .views import (
    show, submit, complete, result
)

app_name = "poll"

urlpatterns = [
    path('<int:poll_id>', show, name="show"),
    path('complete/<int:poll_id>', complete, name="complete"),
    path('result/<int:poll_id>', result, name="result"),
    path('submit/<int:poll_id>', submit, name="submit"),
]
