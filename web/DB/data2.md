# 20230406

======================================================

## Grouping data

> ###### Aggregate function

"집계함수"
여러행의 값을 한개의 값으로 만들고 싶을 때.
COUNT() / AVG() 등등

> ###### GROUP BY clause

**특정 그룹으로 묶인 결과를 생성**
ex) 지역별 평균

```sql
SELECT country, avg(balance) FROM users
GROUP BY country;
```

======================================================

## Changing data

> ###### INSERT statement

- 새 행을 테이블에 삽입

```sql
INSERT INTO classmates
VALUES('홍길동',23,'서울');
```

> ###### UPDATE

- 수정

```sql
UPDATE calssmates
SET name='김철수한무두루미',
    address='제주도'
WHERE rowid=3;
```

> ###### DELETE

- 삭제

```sql
DELETE FROM calssmates
WHERE rowid=2;
```

**soft delete** = 지우긴 지우는데 지웟다는 표시를 해주는거
예를들어 is_deleted 라는 column 만들어서 0과 1로 나눔. 조회할때 0을 조회
**hard delete** = 걍 지움

======================================================

## 정규형

정규형을 잘 지켜서 db를 구축하면

1. 중복최소화
2. 무결성
3. 일관성 보장
4. 독립성
5. 표준화
6. 데이터보안

> ###### 제 1 정규형

- 하나의 속성값이 복수형을 가지면 x
- 

> ###### 제 2 정규형

- 테이블의 테마와 관련 없는 컬럼은 다른 테이블로 분리하는 것

- (테이블에서 부분 함수적 종속성을 제거한 것)
   (부분함수적 종속성)= 키가 아닌 속성이 기본키의 일부분에 종속되는 것

복합키 = 테이블에서 행을 유일하게 구분하기 위해 두 개 이상의 속성을 조합하여 사용하는 기본키

> ###### 제 3 정규형

- 다른 속성에 의존(종속)하는 속성은 따로 분리할 것

## JOIN

> ##### 테이블은 여러 개로 나눠진다

그래서 조회할 때 여러 테이블의 정보를 가져와 참조해야한다

결국 우리가 조회 하려면 모아서 테이블 1개로 만들어야함.

테이블을 연결하는 것이 필요.

JOIN( 두개 이상의 테이블에서 데이터를 가져와 결합하는 것)

> ##### 테이블 합치기

> ###### cross join

- 모든 조합 출력 / 걍 싹다 조합. 잘안씀 너무 데이터가 커짐

```sql
SELECT * FROM articles, users; -- << 이렇게 2개도 가능
```

> ###### INNER JOIN

```sql
-- 두 테이블에서 일치하는 데이터만 결과 출력 

SELECT * FROM articles, users WHERE articles.userid=users.rowid;
-- ↑↑↑↑↑↑↑↑↑↑↑↑↑↑둘다 같은거 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
            -- 근데 밑에 껄 추천. 좀 더 명확하기에
SELECT * FROM articles INNER JOIN users
ON userid=users.rowid;
-- {테이블 1} INNER JOIN {테이블 2} ON {조건식}
```

> ##### 데이터는 일정하지 않다.

> ###### LEFT (OUTER) JOIN

- 왼쪽 테이블의 데이터를 기준으로 오른쪽 데이터 결합. 없으면 NULL

```sql
SELECT * FROM articles LEFT JOIN users
ON userid=users.rowid;
```

> ###### RIGHT (OUTER) JOIN

- LEFT 반대

```sql
SELECT * FROM articles RIGHT JOIN users
ON userid=users.rowid;
```

> ###### FULL OUTER JOIN

?
