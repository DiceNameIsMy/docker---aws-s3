from rest_framework.routers import SimpleRouter
from .views import DropBoxViewset


urlpatterns = [
    
]

router = SimpleRouter()
router.register('accounts', DropBoxViewset)
urlpatterns += router.urls