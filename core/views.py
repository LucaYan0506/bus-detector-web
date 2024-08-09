from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from .predict_video import process_video
from django.conf import settings
import os 

# Create your views here.

def indexView(request):
    return render(request,'index.html')

def detectView(request):
    if request.method == 'POST' and request.FILES.get('video'):
        video = request.FILES['video']
        if video.content_type == 'video/mp4':
            fs = FileSystemStorage()
            filename = fs.save(video.name, video)
            file_url = fs.url(filename)
            model_path = os.path.join(settings.MEDIA_ROOT,'last.pt')
            process_video(os.path.join(settings .MEDIA_ROOT,filename),model_path)
            return HttpResponseRedirect('/media/result.mp4')
        else:
            return JsonResponse({'error': 'Invalid file type'}, status=400)
    return JsonResponse({'error': 'No video file provided'}, status=400)