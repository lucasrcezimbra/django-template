from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/hello", url_name="hello")
def hello(request):
    return {"Hello": "world"}
