from django.shortcuts import render

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "hello_world/index.html", context)
