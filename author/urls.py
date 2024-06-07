from rest_framework import routers

from .views import AuthorViewSet


router = routers.DefaultRouter()
router.register(r"authors", AuthorViewSet, basename="author")

urlpatterns = router.urls

app_name = "author"
