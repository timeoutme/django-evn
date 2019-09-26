from django.shortcuts import render, redirect

items = []


def to_do_lists(request):
    
    if request.method == 'POST':        
        if request.POST['待办事项']:
            item = request.POST['待办事项']
            items.append(item)  
            print(items)          
            return render(request,'to_do_lists.html',{'事项':items})
        else:
            # if request.POST['待办事项'] == '':
            return render(request,'to_do_lists.html',{'错误':'请输入待办事项','事项':items}) 
    elif request.method == 'GET':
        return render(request,'to_do_lists.html',{'事项':items})           
          

def edit_items(request,forloop_counter):
    if request.method == 'POST':
        items[int(forloop_counter)-1] = request.POST['修改']
        return render(request,'edit.html',{'事项':items} )
    elif request.method == 'GET':    
        return render(request,'edit.html',{'事项':items})



def completed_lists(request):
    return render(request,'completed_lists.html')