from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers, authtoken
from rest_framework.authtoken import views

from . import views
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote, PollViewSet, UserCreate, LoginView

app_name = 'polls'

router = routers.DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

urlpatterns = [
    # path('', views.polls_list, name='polls_list'),
    # path('<int:pk>/', views.polls_detail, name='polls_detail'),

    # path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    
    # change to viewsets and routers to less duplication (change line 17)
    path('', include(router.urls)),

    path("users/", UserCreate.as_view(), name="user_create"),
    # path("login/", LoginView.as_view(), name="login"),

    # we can use views from authtoken to login
    path("login/", authtoken.views.obtain_auth_token, name="login"),

]
