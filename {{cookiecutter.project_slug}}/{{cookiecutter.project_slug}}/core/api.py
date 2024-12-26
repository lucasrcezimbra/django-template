{%- if cookiecutter.api == 'Django Ninja' %}
from ninja import NinjaAPI
{%- elif cookiecutter.api == 'Django Ninja CRUD' %}
from django.contrib.auth import get_user_model
from ninja import NinjaAPI, Router
from ninja.orm import create_schema
from ninja_crud.views import (
    CreateModelView,
    ListModelView,
    ModelViewSet,
    RetrieveModelView,
)
{%- endif %}

api = NinjaAPI()


@api.get("/hello", url_name="hello")
def hello(request):
    return {"Hello": "world"}


{%- if cookiecutter.api == 'Django Ninja CRUD' %}
User = get_user_model()

UserIn = create_schema(
    User,
    name="UserIn",
    fields=["username", "first_name", "last_name", "email", "password"],
)

UserOut = create_schema(
    User,
    name="UserOut",
    fields=["first_name", "last_name", "email"],
)


class UserViewSet(ModelViewSet):
    model = User

    list = ListModelView(output_schema=UserOut)
    create = CreateModelView(input_schema=UserIn, output_schema=UserOut)
    retrieve = RetrieveModelView(output_schema=UserOut)


router = Router()
UserViewSet.register_routes(router)
api.add_router(f"/users", router)
{% endif %}
