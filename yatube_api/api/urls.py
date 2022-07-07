from rest_framework.routers import DefaultRouter
from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet
from django.urls import include, path

v1_router = DefaultRouter()

v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register('groups', GroupViewSet, basename='groups')
v1_router.register('follow', FollowViewSet, basename='follow')
v1_router.register('posts/(?P<post_id>\\d+)/comments', CommentViewSet,
                   basename='comments')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
