# 20230411

## N:1(Comment-User)

- 0개 이상의 댓글은 1개의 회원에 의해 작성 될 수 있음

#### 모델 관계 설정


## Many to many relationship



## M:N(Article-User)

N:1의 한계
동일한 환자지만 다른 의사에게 예약하기 위해서는 객체를 하나 더 만들어서 예약을 진행해야 함
 - 새로운 환자 객체를 생성할 수 밖에 없음

외래 키 컬럼에 '1, 2'형태로 참조하는 것은 Integer 타입이 아니기에 불가능

--> 예약 테이블 따로 만들기



M:N 관계로 맺어진 두 테이블에는 변화가 없음
Django의 ManyToManyField은 중개 테이블을 자동으로 생성함
Django의 ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치인자(M:N 관계로 설정할 모델 클래스)가 필요
모델 필드의 RelatedManager를 사용하여 관련 개체를 추가, 제거 또는 만들 수 있음
 - add(), remove(), create(), cleat() ...
