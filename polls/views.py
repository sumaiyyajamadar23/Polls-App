from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Choice, Question
from django.template import loader
from django.urls import reverse
#from .models import Http404
# Create your views here.
def index(request):
   # return HttpResponse("Index view")
   #latest_Q_list=Question.objects.all()
   #latest_Q_list=Question.objects.order_by('-pub_date')[:3]
   latest_Q_list=Question.objects.order_by('pub_date')[:3]
  # output=', '.join([x.q_text for x in latest_Q_list])
  # template=loader.get_template("polls\index.html")
   context={'latest_Q':latest_Q_list,}
   #return HttpResponse(template.render(context,request))
   return render(request,"polls\index.html",context)

def detail(request,question_id):
   #return HttpResponse("This is Quetion %s"%quetion_id)
    try:
        question=Question.objects.get(pk=question_id)
    except:
        raise Http404("Question doesn't exist")
    return render(request,"polls\detail.html",context={'question':question})   

def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,
                      "polls/detail.html",
                     {
                         "question":question,
                         "error_message":"The question is not available."
                     } 
        )
    selected_choice.vote+=1
    selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results",args=(question_id,)))

def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,"polls/results.html",{
                      "question":question
                  })