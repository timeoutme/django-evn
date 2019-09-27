from django.shortcuts import render, redirect

items = [
    {'待办事项':'遛狗', '完成':False},
    {'待办事项':'吃饭', '完成':True},
]


def to_do_lists(request):    
    if request.method == 'POST':        
        if request.POST['待办事项']:
            item = request.POST['待办事项']
            items.append({'待办事项':item, '完成':False})  
            print(items)          
            return render(request,'to_do_lists.html',{'事项':items})
        else:
            # if request.POST['待办事项'] == '':
            return render(request,'to_do_lists.html',{'错误':'请输入待办事项','事项':items}) 
    elif request.method == 'GET':
        return render(request,'to_do_lists.html',{'事项':items})           
          

def delete(request,forloop_counter):
    del items[int(forloop_counter)-1]
    return redirect('待完成事项')


def line(request,forloop_counter):
    items[int(forloop_counter)-1]['完成'] = True
    return redirect('待完成事项')


def edit(request,forloop_counter):
    if request.method == 'POST':
        items[int(forloop_counter)-1]['待办事项'] = request.POST['修改']
        return redirect('待完成事项')
    elif request.method == 'GET':
        return render(request,'edit.html')    


def cexiao(request,forloop_counter):
    items[int(forloop_counter)-1]['完成'] = False
    return redirect('待完成事项')

def completed_lists(request):
    return render(request,'completed_lists.html',{'事项':items})