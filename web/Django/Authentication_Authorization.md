# 20230322

## 인증과 권한 (AUTH)

Django authentication system(인증 시스템)은 인증과 권한 부여를 함께 제공(처리)하며, 이러한 기능을 일반적으로 인증 시스템이라 한다.
필수 구성은 settings.py에 이미 포함되어있고, INSTALLED_APPS에서 확인가능. django.contrib.auth

> ###### 개요

- 인증
- 신원 확인, 사용자가 자신이 누구인지 확인하는 것
- 권한,허가
- 권한 부여, 인증된 사용자가 수행할 수 있는 작업을 결정

> ###### 사전 설정

- 두번째 app accounts 생성 및 등록

```bash
$ python manage.py startapp accounts
# [1]생성 후 settings.py의 INSTALLED_APPS에 추가.

# [2]url 분리 및 매핑 (프로젝트 url에서 accounts url로)

```

## Custom User model

> ###### 개요

- Custom User Model로 대체하기.
- 기본 User Model을 필수적으로 Custom User model로 대체하는 이유?
- django에서 제공하는 user model의 기본 인증 요구사항이 적절하지 않을 수 있기에. ex- 회원가입시 이름보다 email이 더 적합할 때
- AUTH_USER_MODEL 설정값으로 재정의 가능

> ###### AUTH_USER_MODEL

- 프로젝트에서 User를 나타낼 때 사용하는 모델
- 첫번 째 마이그레이션 전에 확정 지어야함.
  [중간 변경은 권장하지 않음/ 다시 설정해줄게 너무 많다.]

```bash
# accounts/models.py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# settings.py에 적어주기
AUTH_USER_MODEL = 'accounts.User'

# admin.py에 커스텀 User 모델 등록. 기본 User 모델이 아니기 때문에, 등록하지않으면 admin site에 출력x
# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

## HTTP

> ###### HTTP 특징

1. 비 연결 지향(connectionless)

- 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
  - 예를 들어 우리가 네이버 메인 페이지를 보고 있을 때 우리는 네이버 서버와 연결되어 있는 것이 아님
  - 네이버 서버는 우리에게 메인 페이지를 응답하고 연결을 끊은 것

2. 무상태(stateless)

- 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지 되지 않음
- 클라이언트와 서버가 주고받는 메시지들은 서로 완전히 독립적

그래서 HTTP에 뭔가 기능을 추가해서 상태를 가질수 있게 만든다. = 쿠키, 세션
ex- 로그인 상태를 유지.

#### Cookie

아주 작은 Data 조각

HTTP 쿠키는 상태가 있는 세션을 만들도록 해 줌

> ###### 개념

- 사용자가 웹사이트를 방문할 경우, 해당 웹사이트의 서버를 통해 사용자의 컴퓨터에 설치되는 작은 기록 정보 파일

> ###### 쿠키 사용 목적

1. 세션 관리

- 로그인, 공지 하루 안보기, 장바구니, 팝업체크 등

2. 개인화

- 사용자 선호, 테마 등의 설정

3. 트래킹

- 사용자 행동을 기록 및 분석

> ###### 세션(Session)

- 사이트와 특정 브라우저 사이의 'state(상태)'를 유지시키는 것 (HTTP는 무상태)
- 클라이언트가 서버에 접속하면 서버가 특정 session id 발급. 클라이언트는 이를 쿠키에 저장
- session id는 세션을 구별하기위해 필요

## Login

- Session을 Create 하는 과정

> AuthenticationForm

- 로그인을 위한 빌트인 form

> ###### login()

- login(request, user, backend=None)
- 인증된 사용자를 로그인 시키는 로직
- View 함수에서 사용
- HttpRequest 객체/ User 객체가 필요

> ###### 로그인 로직 작성

- view 함수 login과의 충돌을 방지하기 위해 import한 login 함수 이름을 auth_login으로 변경해서 사용

> 세션 데이터 확인하기

로그인 후 개발자 도구와 DB에서 django로부터 발급받은 세션 확인

- django_session테이블에서 확인
- 브라우저 개발자 도구에서 확인 개발자도구-Application- Cookies

settings - context processor
django가 자주 사용하는 데이터 목록을 미리 템플릿에 로드해 둠/ {{user}} 등

# Logout

로그아웃은 Session을 Delete하는 과정

- logout(request)
- 다음 2가지 일을 처리
- 1.  현재 요청에 대한 session data를 DB에서 삭제
- 2.  클라이언트의 쿠키에서도 sessionid를 삭제
