from django.urls import path, include
from .views import SingUpView

urlpatterns = [
    path('signup/', SingUpView.as_view(), name='signup'),
]
