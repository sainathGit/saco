from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse

def index(request):
	questions = Question.objects.all()
	context = {'questions': questions}
		 
	return render(request, 'polls/index.html', context)



def detail(request, question_id):
			
#question = get_object_or_404(Question, pk=question_id)
#find the prev and next and present questions

	question = None 
	prev_question_id = -1
	next_question_id = -1
	
	questions = Question.objects.all()

	for i,q in enumerate(questions):
		if q.id == question_id:
			question = q
			if i != 0:
				prev_question_id = questions[i-1].id
			if i != len(questions)-1: 
				next_question_id = questions[i+1].id
			break

	#arise 404 if question is not been found

	return render(request,'polls/detail.html',{'question':question,'prev_question_id':prev_question_id,'next_question_id':next_question_id})



def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
					'question' : question,
					'error_message': "you didn't select a choice.",
					})
	else:
		selected_choice.votes += 1
		selected_choice.save()

		return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))

