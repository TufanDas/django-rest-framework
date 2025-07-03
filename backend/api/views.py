from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def api_home(request, *args, **kwargs):
    return JsonResponse({"messege" : "Hi there this is the django api response."})

from django.http import JsonResponse
import json

def request_demo_view(request):
    # Get query parameter from URL: ?search=...
    search_query = request.GET.get('search')

    # Get POST form data (only works if content type is form)
    post_name = request.POST.get('name')

    # Read raw body (e.g., when sending JSON)
    try:
        data = json.loads(request.body)
        body_name = data.get('name')
    except:
        body_name = None

    # Access headers
    user_agent = request.headers.get('User-Agent')
    auth_token = request.headers.get('Authorization')

    # Content-Type (e.g. application/json)
    content_type = request.content_type

    return JsonResponse({
        "search_query": search_query,
        "post_name": post_name,
        "body_name": body_name,
        "user_agent": user_agent,
        "auth_token": auth_token,
        "content_type": content_type
    })