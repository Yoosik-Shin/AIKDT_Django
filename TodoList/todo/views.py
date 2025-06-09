from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q

from .models import * # 현재 모듈의 models의 모든 모델 import

# Create your views here.
def index(request):
  print('메인 화면...')
  return render(request, 'todo/index.html', {})

def todo(request):
  print('할 일 목록 화면...')

  # 할 일 목록 조회
  # Todo 모델의 대기 목록 조회
  wait_list = Todo.objects.filter(status='WAIT')
  # Todo 모델의 진행 목록 조회
  ing_list = Todo.objects.filter(Q(status='ING') | Q(status='DONE')).order_by('-status')
  # todos = Todo.objects.all()  # Todo 모델의 모든 데이터 조회
  content = {'wait_list' : wait_list, 'ing_list' : ing_list}
  # render(request, 템플릿 경로, 데이터{딕셔너리컬렉션 형태})
  #                             └─ 딕셔너리를 담았다면 그냥 변수명만 입력하면 됨
  # - 데이터{} : 템플릿에 데이터를 전달
  return render(request, 'todo/todo.html', content)

def create(request):
  print('할 일 등록 됨')

  # POST 방식으로 전송한 파라미터 가져오기?
  title = request.POST['title']
  new_todo = Todo(title = title) # title에 가져온 title 넣어주기
  new_todo.save() # 위에서 가져온거 저장하기 DB에 저장

  # 등록 요청

  # 할 일 목록('todo')으로 리다이렉트
  return HttpResponseRedirect(reverse('todo'))

def delete(request):
    print('삭제 요청 됨')

    # 파라미터
    no = request.POST['no']
    print('no : {}'.format(no))
    try:
        todo = Todo.objects.get(no=no)
        todo.delete() # 할 일 삭제 요청
    except Todo.DoesNotExist:
      print('삭제할 할 일이 없습니다.')
    return HttpResponseRedirect(reverse('todo'))

def ing(request):
    print('진행 상태로 변경...')
    no = request.POST['no']
    print('no : {}'.format(no))
    try:
        todo = Todo.objects.get(no=no)
        # 할 일 상태 수정
        todo.status = 'ING'
        todo.save()
    except Todo.DoesNotExist:
      print('수정할 할 일이 없습니다.')
    return HttpResponseRedirect(reverse('todo'))

def done(request):
    print('완료 상태로 변경...')
    no = request.POST['no']
    print('no : {}'.format(no))
    try:
        todo = Todo.objects.get(no=no)
        if todo.status == 'DONE':
          todo.status = 'ING'
        else:
          todo.status = 'DONE'
        # 할 일 상태 수정
        todo.save()
    except Todo.DoesNotExist:
      print('완료할 할 일이 없습니다.')
    return HttpResponseRedirect(reverse('todo'))

def wait(request):
    print('대기 상태로 변경...')
    no = request.POST['no']
    print('no : {}'.format(no))
    try:
        todo = Todo.objects.get(no=no)
        if todo.status == 'DONE' or todo.status == 'ING':
          todo.status = 'WAIT'
        else:
          todo.status = 'DONE'
        # 할 일 상태 수정
        todo.save()
    except Todo.DoesNotExist:
      print('완료할 할 일이 없습니다.')
    return HttpResponseRedirect(reverse('todo'))