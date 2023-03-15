# 20230314

#### Framework란

- 서비스 개발에 필요한 기능들을 미리 구현해서 모아 놓은 것
- Frame(뼈대, 틀) + Work(일하다)
- 소프트웨어의 생산성과 품질을 높임

## 클라이언트-서버 구조

- 오늘날 대부분의 웹서비스는 클라이언트-서버 구조를 기반으로 동작
- 클라이언트
  - 웹 사용자의 인터넷에 연결된 장치(wifi에 연결된 컴퓨터 또는 모바일)
  - Chrome 또는 Firefox와 같은 웹 브라우저
  - 서비스를 요청하는 주체 
- 서버
  - 웹페이지, 사이트 또는 앱을 저장하는 컴퓨터
  - 클라이언트가 웹페이지에 접근하려고 할 때 서버에서 클라이언트 컴퓨터로 웹페이지 데이터를 응답해 사용자의 웹브라우저에 표시됨
  - 요청에 대해 서비스를 응답하는 주체
  - Django는 서버를 구현하는 웹 프레임 워크

## Django 설치

> $ pip install django==3.2.18

- 버전을 안붙이면 가장 최신 버전이 설치. 버전을 명시

프로젝트 생성
$ django-admin startproject firstpjt

서버 실행
$ python manage.py runserver

## 가상환경

> #### 패키지와 가상환경

각각의 패키지를 하나의 환경에 담아야 한다면?

> #### 가상환경 사용

가상환경 생성
git bash에서 python -m venv venv

가상환경 활성화(ON)
source ./venv/Scripts/activate

가상환경 비활성화(OFF)
deactivate

> #### 가상환경 사용하기

가상환경이란? 프로젝트별 패키지를 독립적으로 관리하기 위한 것
내 프로젝트를 다른 사람이 실행하려면? 모든 패키지를 다 설치해야한다.

가상환경 패키지 목록 저장
pip freeze > requirements.txt

파일로부터 패키지 설치
pip install -r requirements.txt

생성된 프로젝트 구조
 __init__.py
 asgi.py 
 settings.py = Django 프로젝트 설정을 관리
 urls.py
 wsgi.py
manage.py = Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티

> #### Django Application

애플리캐이션(앱) 생성
$ python manage.py startapp articles
  일반적으로 애플리케이션 이름은 '복수형'으로 작성하는 것을 권장

생성된 애플리캐이션 구조
__init__.py
admin.py
apps.py 딱히
models.py 애플리케이션에서 사용하는 Model을 정의하는 곳. MTV의 M
tests.py 그런가보다 테스트코드 작성하는 곳
views.py 앱의 로직 기능을 적는곳. view함수들이 정의되는곳 MTV의 V에 해당( T는 Template 보여지는. )

> #### 애플리캐이션 등록

앱을 사용하기 위해서는 반드시 (settings.py)의 INSTALLED_APPS 리스트에 앱 이름을 추가해야함.

#### project & Application

- project
  -
  - 프로젝트는 앱의 집합
  - 프로젝트에는 여러 앱이 포함될 수 있음
  - 앱은 여러 프로젝트에 이쓸 수 있음
- App
  - 앱은 실제 요청을 처리하고 페이지를 보여주는 등의 역할을 담당
  - 앱은 하나의 역할 및 기능 단위로 작성하는 것을 권장함

> #### Django의 세가지 구조

Model View Template

프로젝트의 urls에 작성

```
from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', views.index),
]
```

app의 views 파일에 작성

```
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1> ~~~~ ~ ~ ~ ~ ~</h1>")
```

> #### Templates

- 실제 내용을 보여주는데 사용되는 파일
- 파일의 구조나 레이아웃을 정의
- Template 파일의 기본 경로
  - app 폴더 안의 templates 폴더
  - app_name/templates/app_name
    템플릿 폴더 이름은 반드시 templates라고 지정해야 함

> #### render()
> 
> render(request, template_name, context)

- 주어진 템플릿을 주어진 컨텍스트 데이터와 결합하고 렌더링 된 텍스트와 함께 HttpResponse(응답) 객체를 반환하는 함수
1. request
   - 응답을 생성하는데 사용되는 요청 객체
2. template_name
   - 템플릿의 전체 이름 또는 템플릿 이름의 경로
3. context
   - 템플릿에서 사용할 데이터 (딕셔너리 타입으로 작성)

```
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'articles/index.html')
```

> 코드 작성 순서

- Django에서의 코드 작성은 URL -> View -> Template순으로 작성
- "데이터의 흐름 순서"


프로젝트 위치 옮기는건 가능.
프로젝트 이름 바꾸는건 불가능.
