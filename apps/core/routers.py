# apps/core/routers.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.routers import DefaultRouter
from .viewsets import UserViewSet

# Local imports
# from ..app_django.routers import router_list as app_django_router
from ..product.routers import product

tuple_ = (
    (r"users", UserViewSet),
  
)
# Create your routers here.
# routers_tuples = (app_django_router,)
routers_tuples = (tuple_,product,)
routers_lists = sum(
    # [list(router_tuple) for router_tuple in routers_tuples], [])
    [list(router_tuple) for router_tuple in routers_tuples], [])

router = DefaultRouter()

for router_list in sorted(routers_lists):
    router.register(router_list[0], router_list[1])
    #router.register(router_list[0], router_list[1], base_name=router_list[0])
