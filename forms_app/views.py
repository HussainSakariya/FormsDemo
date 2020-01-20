from django.shortcuts import render,get_object_or_404,redirect
from .forms import *
from .models import *

# Create your views here.
def reg(request):
    if request.method=='POST':
        # frm=reg_forms(request.POST)
        # if frm.is_valid():
        #     frm.save()
        #     return redirect("/display")  
        frm=add_img_forms(request.POST,request.FILES)
        if frm.is_valid():
            frm.save()
            return redirect("/display")
    else:
        frm=add_img_forms()
        return render(request,'register.html',{'frm':frm})
        # frm=reg_forms()
        # return render(request,'register.html',{'frm':frm})

def edit(request,id):
    frm=get_object_or_404(reg_tbl,id=id)
    if request.method=='POST':
        user_frm=reg_forms(request.POST,instance=frm)
        if user_frm.is_valid:
            user_frm.save()
            return redirect('/display')    
    else:
        user_frm=reg_forms(instance=frm)
        return render(request,'edit.html',{'user_frm':user_frm})    

def delete(request,id):
    user=reg_tbl.objects.get(id=id)
    user.delete()
    return redirect('/display')
    
def display(request):
    user=reg_tbl.objects.all()
    img=add_image.objects.all()
    return render(request,'display.html',{'user':user,'img':img})