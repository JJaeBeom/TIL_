INSTALLED_APPS -> django.contrib.staticfiles 포함 확인

settings.py  STATIC_URL 정의

static 폴더에 정적파일 위치

로드 태그


1. 장고 프로젝트 환경 설정
 - 프로젝트 폴더 생성
 - 프로젝트 폴더에 가상환경 생성 및 활성화
 - 가상환경에 프로젝트에 필요한 모듈
 - .gitignore 파일 생성하기
2. 장고 프로젝트/애플리케이션 생성
 - 장고 프로젝트 생성
 - 장고 프로젝트 앱 생성 및 등록
 - 서버 연결 확인
3. 기본 셋팅
 - 기본 템플릿 base.html 생성
 - 앱별로 urls 따로 관리하도록 설정해주기
4. 메인 페이지 생성하기
 - urls -> views -> templates 순서로 요청에 따른 응답 정의하기
5. 데이터베이스 테이블, 모델 생성하기
 - 모델 클래스 정의하기
  - models 모듈의 Model 클래스를 상속받아 Article 클래스를 생성한다.
  - Article 클래스 안에 title, content, created_at, updated_at 등 필드를 생성한다.
 - 생성된 클래스를 실제 DB에 반영하기
  - python manage.py makemigrations
  - python manage.py migrate

6. 관리자 페이지
 - 관리자 계정 생성하기
  - python manage.py createsuperuser
 - 생성한 모델 관리자 페이지에 등록
7. 사용자가 입력한 데이터 DB에 저장하기
 - 모델 폼 생성하기
 - 사용자가 데이터를 입력할 웹페이지 생성하기
 - 추가작업: 사용자 편의 기능 추가
8. detail 페이지 만들기
 - urls -> views -> templates 순서로
 - 추가작업:
9. update 페이지 생성
 - 추가작업:
10. DB에서 데이터 삭제하기

11. USER 모델 생성하기

12. 로그인/로그아웃 기능 추가하기
