from api.models import CourseResource, CategoryResource
from tastypie.api import Api
from django.urls import path, include

api = Api(api_name='v1')
api.register(CategoryResource())
api.register(CourseResource())

# api/v1/courses/      GET, POST
# api/v1/courses/1/    GET, DELETE
# api/v1/categories/   GET
# api/v1/categories/1/ GET

# for POST, DELETE add header
# Key: Authorization
# Value: ApiKey annazamyrovska:45646465dsdsd

urlpatterns = [
    path('', include(api.urls), name='index')
]
