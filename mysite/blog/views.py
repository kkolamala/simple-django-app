from django.http import JsonResponse
#import json
# Create your views here.

def index(request):
    data = {
        "Name":'Kris',
        "Track":'Backend Python Track',
        "Message":'The learning materials and instructions are good'
    }
    
    return JsonResponse(data)
 
    # return HttpResponse(json.dumps(data),headers={
    #     'Content-Type':'application/json',
    #     'Content-Description':'About myself and my track info'
    # })
