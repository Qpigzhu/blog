from django.shortcuts import render_to_response

def home_datil(request):
    context = {}
    return render_to_response('home.html',context)