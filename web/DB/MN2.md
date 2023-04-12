# 20230412

## M:N(User-User)

#### Profile

## Fixtures

> 초기 데이터의 필요성

- 협업하는 A, B 유저
  1. A가 먼저 프로젝트를 작업 후 github에 push한다.
     - gitignore 설정으로 인해 DB는 업로드하지 않기 때문에 A가 개발하면서 사용한 데이터는 올라가지 않는다.
  2. B가 github에서 A push한 프로젝트를 pull (혹은 clone) 한다.
     - 마찬가지로 프로젝트는 받았지만 A가 생성하고 조작한 데이터는 없는 빈 프로젝트를 받게 된다.
- 이처럼 django 프로젝트의 앱을 처음 설정할 때 동일하게 준비 된 데이터로 데이터베이스를 미리 채우는 것이 필요한 순간이 있다.
- django에서는 fixtures를 사용해 앱에 초기 데이터(initial data)를 제공할 수 있다.
- 즉, migrations와 fixtures를 사용하여 data와 구조를 공유하게 된다.

#### dumpdata

- 여러 모델을 하나의 json 파일로 만들 수 있음
  $ python manage.py dumpdata articles.article > articles.json

4칸씩 들여써서 보여줘.(가시성) --indent 4 
$ python manage.py dumpdata articles.article --indent 4  > articles.json

- 몇가지 모델을 하나의 json 파일로 만들수 있음
  $ python manage.py dumpdata --indent 4 articles.article articles.comment accounts.user > data.json

- 모든 모델을 하나의 json 파일로 만들수도 있음
  $ python manage.py dumpdata --indent 4 > data.json

#### loaddata

fixtures 기본 경로
app_name/fixtures/

$ python manage.py loaddata articles.json users.json comments.json

오류뜨면 해결 방법.
dumpdata 시 추가 옵션 작성
$ python -Xutf8 manage.py dumpdata [생략]

메모장 활용

1. 메모장으로 json파일 열기
2. 다른이름으로 저장 클릭/ 모든파일
3. 인코딩을 UTF8로 선택 후 저장

# [참고] loaddata를 하는 순서.

관통pjt할때 에러나면 보면서.
loadtata를 한번에 실행하지 않고 하나씩 실행한다면 모델 관계에 따라 순서가 중요할 수 있음.

- comment는 article에 대한 key 및 user에 대한 key가 필요
- article은 user에 대한 key가 필요
  - 즉, 현재 모델 관계에서는 user -> article -> comment 순으로 data를 넣어야 오류가 발생하지 않음

## Improve Query

> ###### Django ORM

- 장점
  
  - SQL 몰라도 됨
  - SQL을 사용하는 대신 객체 지향적으로 데이터를 조회할 수 있다.
  - 재사용 및 유지보수가 쉽다.
  - DBMS에 대한 의존도가 떨어진다.

- 단점
  
  - 복잡한 SQL문을 그대로 재현하기 어려움
  - 멋모르고 사용하면 이상한 쿼리 나감.(N+1 problem이 대표적)

- 특징
  
  - django ORM은 기본적으로 Lazy loading 전략을 사용함.
    - ORM을 작성하면 Database에 Query하는 것이 아니라, 미루고 미루다가 실제로 데이터를 사용할 때 Database에 Query를 날린다.