from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from watchlist_app.api.views import movie_list,movie_details
from watchlist_app.api.views import (
    WatchListAV,
    WatchDetailAV,
    StreamPlatformAV,
    StreamPlatformDetailAV,
    ReviewList,
    ReviewCreate,
    ReviewDetail,
    StreamPlatformVS,
    UserReview,
    WatchListFilter
)

router = DefaultRouter()
router.register('stream',StreamPlatformVS,basename='streamplatform')

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="movie-list"),
    path("<int:pk>/", WatchDetailAV.as_view(), name="movie-details"),
    path("list2/", WatchListFilter.as_view(), name="movie-list-filter"),

    path('',include(router.urls)),

    # path("stream/<int:pk>", StreamPlatformDetailAV.as_view(), name="stream-details"),
    # path("stream/", StreamPlatformAV.as_view(), name="stream"),

    path("<int:pk>/review-create/", ReviewCreate.as_view(), name="review-create"),
    path("<int:pk>/review/", ReviewList.as_view(), name="review-list"),
    path("review/<int:pk>/", ReviewDetail.as_view(), name="review-details"),

    #path('reviews/<str:username>/',UserReview.as_view(),name='user-review-detail')
    path('reviews/',UserReview.as_view(),name='user-review-detail')
    # path('review/',ReviewList.as_view(),name='review-list'),
    # path('review/<int:pk>',ReviewDetail.as_view(),name='review-details')
]
