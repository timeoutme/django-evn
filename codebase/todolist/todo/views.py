from django.shortcuts import render, redirect
from .models import Toto

items = [
    {'待办事项':'遛狗', '完成':False},
    {'待办事项':'吃饭', '完成':True},
]


def to_do_lists(request):    
    if request.method == 'POST':        
        if request.POST['待办事项']:
            item = request.POST['待办事项']
            a = Toto(items = item)  
            a.save()                    
            return render(request,'to_do_lists.html',{'事项':Toto.objects.all()})
        else:
            # if request.POST['待办事项'] == '':
            return render(request,'to_do_lists.html',{'错误':'请输入待办事项','事项':Toto.objects.all()}) 
    elif request.method == 'GET':
        return render(request,'to_do_lists.html',{'事项':Toto.objects.all()})           
          

def delete(request,item_id):
    # del items[int(item_id)]
    Toto.objects.get(id=item_id).delete()
    return redirect('待完成事项')


def line(request,item_id):
    # items[int(forloop_counter)-1]['完成'] = True
    a = Toto.objects.get(id=item_id)
    a.achieve = True
    a.save()
    return redirect('待完成事项')


def edit(request,item_id):
    if request.method == 'POST':
        # items[int(forloop_counter)-1]['待办事项'] = request.POST['修改']
        a = Toto.objects.get(id=item_id)
        a.items = request.POST['修改']
        a.save()
        return redirect('待完成事项')
    elif request.method == 'GET':
        return render(request,'edit.html')    


def cexiao(request,item_id):
    # items[int(forloop_counter)-1]['完成'] = False
    a = Toto.objects.get(id=item_id)
    a.achieve = False
    a.save()
    return redirect('待完成事项')

def completed_lists(request):
    return render(request,'completed_lists.html',{'事项':Toto.objects.all()})