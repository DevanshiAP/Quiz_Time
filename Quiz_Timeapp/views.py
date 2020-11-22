from django.shortcuts import render,redirect
from .models import Questions
from .forms import Questionsfrom
from django.core.paginator import Paginator


# Create your views here.
lst=[]
anslist=[]
answers = Questions.objects.all()

for i in answers:
    anslist.append(i.answer)

def Quiz(request):
    quiz_questions=Questions.objects.all()
    paginator = Paginator(quiz_questions,1)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page =1
    try:
        Que = paginator.page(page)
    except(Emptypage,InvalidPage):
        Que = paginator.page(paginator,num_pages)
    return render(request,"Quiz.html",{'Quiz_Qestion':quiz_questions,'paginatorque':Que})

def result(request):
    score = 0
    for i in range(len(lst)):
        if lst[i] == anslist[i]:
            score+=1
    return render(request,"result.html",{'score':score})

def welcome(request):
    lst.clear()
    return render(request,"Welcome.html")

def adminpage(request):
    if request.method == "POST":
        que = Questionsfrom(request.POST)
        if que.is_valid():
            que.save()
            return redirect('Questiondata')
    else:
        que = Questionsfrom()
        return render(request,"admin.html",{'adminquestion':que})
        
def Questionupdate(request,id):
    if request.method == "POST":
        Que = Questions.objects.get(id=id)
        Ques = Questionsfrom(request.POST)
        if Ques.is_valid():
            Ques.save()
            return redirect('Questiondata')
    else:
        Que = Questions.objects.get(id=id)
        Ques = Questionsfrom(instance=Que)
        return render(request,"Questionupdate.html",{'QueUpdate':Ques})

def Questiondelete(request,id):
    Que = Questions.objects.get(id=id)
    Que.delete()
    return redirect('Questiondata')

def Questiondata(request):
    que = Questions.objects.all()
    return render(request,"Questiondata.html",{'data':que})

def saveans(request):
    ans = request.GET['ans']
    print("&&&&&&&&&&&&&&&&&&&&&&")
    print(ans)  
    lst.append(ans)