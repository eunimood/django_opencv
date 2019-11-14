from django.shortcuts import render
from django.shortcuts import redirect
# from .forms import UploadImageForm
from django.core.files.storage import FileSystemStorage
from .forms import ImageUploadForm
from django.conf import settings
from .cv_functions import cv_detect_face

def first_view(request):
    return render(request, 'opencv_webapp/first_view.html', {})

def detect_face(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) # DB에 실제로 저장하기 전에 추가로 Form(post)에 다른 데이터 추가 가능
            post.save() # DB에 실제로 Form에 모아진 데이터를 저장

            imageURL = settings.MEDIA_URL + form.instance.document.name
            cv_detect_face(settings.MEDIA_ROOT_URL + imageURL) # 추후 구현 예정

            return render(request, 'opencv_webapp/detect_face.html', {'form':form, 'post':post})
            # post는 save() 후 DB에 저장된 ImageUploadModel 클래스 객체 자체를 갖고 있게 됨 (값이 있음 == True)
    else:
         form = ImageUploadForm()
    return render(request, 'opencv_webapp/detect_face.html', {'form':form})




def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            context = {'form': form, 'uploaded_file_url': uploaded_file_url}
            return render(request, 'opencv_webapp/upload_image.html', context)
    else: # request.method == 'GET'
        form = UploadImageForm()
        context = {'form': form}
        return render(request, 'opencv_webapp/upload_image.html', context)
