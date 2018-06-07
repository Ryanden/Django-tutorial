from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader

# Create your views here.
from .models import Question


def index(request):

    # DB에 있는 Question 중에 가장 최근에 발행(pub_date)로 된 순서대로 최대 5개에 해당하는 QuerySet
    # latest_question_list 변수에 할당
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # latest_question_list 의 각 Question 의 question_text 들을 ','로 연결시킨 문자열을 output 변수에 할당
    # output = ', '.join([q.question_text for q in latest_question_list])

    # 장고의 template 설정에 정의 된 방법으로,
    # 주어진 인자에 해당하는 템플릿 파일을 가지는 인스턴스를 생성, 리턴
    template = loader.get_template('polls/index.html')

    context = {
        'latest_question_list': latest_question_list,
    }

    #
    # html = template.render(context, request)
    #
    # return HttpResponse(html)

    return render(request, 'polls/index.html', context)

    # 만들어진 질문 제목들을 모은 문자열을 HttpResponse 클래스의 생성로 전달, 인스턴스를 리턴
    # return HttpResponse(output)


def custom_get_object_or_404(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        raise Http404()


def detail(request, question_id):

    try:
        question = Question.objects.get(id=question_id)

    except Question.DoesNotExist:
        raise Http404('파일없어')

    question = get_object_or_404(Question, id=question_id)

    question = custom_get_object_or_404(Question, id=question_id)

    context = {
        'question': question
    }

    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
