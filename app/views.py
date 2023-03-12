from django.http import JsonResponse
from .utils import firebase_data
def hello_world(request):
    addreass = request.GET.get('addreass')
    date = request.GET.get('date')
    gamename = request.GET.get('gamename')
    #print(path_lodu,'------------------111')
    if addreass and date and gamename:
        fir_db = firebase_data(addreass,date,gamename)    
        return JsonResponse({'sucess': fir_db})
    else:
        return JsonResponse({'error': 'Missing string parameter'}, status=400)
    

