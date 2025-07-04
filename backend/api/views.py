from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from products.models import Product
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """ Django API view """

    if request.method != "POST":
        return Response({"detailed" : "GET not allowed."},status=405)
    product_data = Product.objects.all().order_by("?").first()
    data = {}

    if product_data:
        # data['id'] = product_data.id # refault id field provoded by django model
        # data['title'] = product_data.title
        # data['content'] = product_data.content
        # data['price'] = product_data.price
        data = model_to_dict(product_data,fields=['id','title','price'])
        
    return Response(data)

# from django.http import JsonResponse
# import json

# def request_demo_view(request):
#     # Get query parameter from URL: ?search=...
#     search_query = request.GET.get('search')

#     # Get POST form data (only works if content type is form)
#     post_name = request.POST.get('name')

#     # Read raw body (e.g., when sending JSON)
#     try:
#         data = json.loads(request.body)
#         body_name = data.get('name')
#     except:
#         body_name = None

#     # Access headers
#     user_agent = request.headers.get('User-Agent')
#     auth_token = request.headers.get('Authorization')

#     # Content-Type (e.g. application/json)
#     content_type = request.content_type

#     return JsonResponse({
#         "search_query": search_query,
#         "post_name": post_name,
#         "body_name": body_name,
#         "user_agent": user_agent,
#         "auth_token": auth_token,
#         "content_type": content_type
#     })