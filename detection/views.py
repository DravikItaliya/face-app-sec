from django.shortcuts import render
from django.http.response import StreamingHttpResponse

# Create your views here.
def home(request):
    return render(request, 'detection/home.html')


def facecam_feed():
    return None