from django.shortcuts import render

# Create your views here.

def survey_list(request):
    return render(request,'survey_list.html')