# 20230320

#### Admin-site

> 개요

- Django의 가장 강력한 기능 중 하나인 automatic admin interface
- '관리자 페이지'
- 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
- 모델 class를 admin.py에 등록하고 관리
- 레코드 생성 여부 확인에 매우 유용하며 직접 레코드를 삽입할 수도 있음

$ python manage.py createsuperuser
username은 admin으로.
email은 admin@admin.kr
Password: pass1234로 통일

> admin에 모델 클래스 등록

- 모델의 record를 보기 위해서는 admin.py에 등록 필요

#### CRUD with view functions

> 개요

- 이전에 익힌 QuerySet API를 통해 view 함수에서 직접 CRUD 구현하기

#### 사전 준비

> base 템플릿 작성

- bootstrap CDN 및 템플릿 추가 경로 작성

> url 분리 및 연결

-

> index 페이지 작성

-
