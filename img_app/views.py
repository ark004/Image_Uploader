from django.shortcuts import render,redirect
from .forms import ImageForm
from .models import image
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.
def home(request):
    if request.method == "POST":
     form = ImageForm(request.POST, request.FILES)
     if form.is_valid():
      form.save()
    form = ImageForm()
    img = image.objects.all()
    paginator=Paginator(img,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)


    return render(request,'myapp/home.html',{'img':img , 'form':form ,'pg':pro })


def detail(request,img_id):
    imgpr=  image.objects.get(id=img_id)  
    return render(request,'myapp/imgview.html',{'pr':imgpr})

def delete(request,taskid):
    task=image.objects.get(id=taskid)
    if request.method=="POST":
        task.delete()
        return redirect('/')
    return render(request,'myapp/del.html',{'task':task})
