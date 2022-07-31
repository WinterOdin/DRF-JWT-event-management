from .views import EventViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", EventViewset, basename="event")
urlpatterns = router.urls


# here are the urls from my previous solutions
# urlpatterns = [
#     path('posts/', PostDetail.as_view(), name='detailcreate'),
#     path('search/', PostListDetailfilter.as_view(), name='postsearch'),
#     path('', PostList.as_view(), name='listcreate'),
# ]


# urlpatterns = [

#     path('search/', EventDetailFilter.as_view(), name='postsearch'),
#     path('', EventList.as_view(), name='listcreate'),
# ]
