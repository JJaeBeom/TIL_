# 20230322

## 인증과 권한
Django authentication system(인증 시스템)은 인증과 권한 부여를 함께 제공(처리)하며, 이러한 기능을 일반적으로 인증 시스템이라 한다.
필수 구성은 settings.py에 이미 포함되어있고, INSTALLED_APPS에서 확인가능. django.contrib.auth

> ###### 개요
- 인증
 - 신원 확인, 사용자가 자신이 누구인지 확인하는 것
- 권한,허가
 - 권한 부여, 인증된 사용자가 수행할 수 있는 작업을 결정

>###### 사전 설정
- 두번째 app accounts 생성 및 등록
```bash
$ python manage.py startapp accounts
# [1]생성 후 settings.py의 INSTALLED_APPS에 추가.

# [2]url 분리 및 매핑 (프로젝트 url에서 accounts url로)

```

## Custom User model
>###### 개요
- Custom User Model로 대체하기.
- 기본 User Model을 필수적으로 Custom User model로 대체하는 이유?
 - django에서 제공하는 user model의 기본 인증 요구사항이 적절하지 않을 수 있기에. ex- 회원가입시 이름보다 email이 더 적합할 때
 - AUTH_USER_MODEL 설정값으로 재정의 가능

>###### AUTH_USER_MODEL
- 프로젝트에서 User를 나타낼 때 사용하는 모델
