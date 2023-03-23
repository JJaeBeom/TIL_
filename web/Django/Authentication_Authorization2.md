# 20230323

## Authentication with User

> ###### 개요

- User Object 와 User CRUD에 대한 이해
- 회원 가입, 회원 탈퇴, 회원정보 수정, 비밀번호 변경

#### 회원가입

- 회원가입은 User를 Create하는 것이며 UserCreationForm built-in form을 사용

> ###### UserCreationForm

- 주어진 username과 password로 권한이 없는 새 user를 생성하는 ModelForm
- 3개의 필드를 가짐

1.  username (form the user model)
2.  password1
3.  Password2

```bash
# accounts/urls.py
app_name = 'accounts'
urlpatterns
```

#### Custom user & Built-in auth forms

> ###### AbstractBaseUser의 모든 subclass와 호환되는 forms

- 아래 Form 클래스는 User 모델을 대체하더라도 커스텀 하지 않아도 사용가능

1. AuthenticationForm
2. SetPasswordForm
3. PasswordChangeForm
4. AdminPasswordChangeForm

- 기존 User모델을 참조하는 Form이 아니기 때문

> ###### 커스텀 유저 모델을 사용하려면 다시 작성하거나 확장해야하는 forms

1. UserCreationForm
2. UserChangeForm

- 두 form 모두 class Meta: model = User가 등록된 form이기 때문에 반드시 커스텀(확장)해야함

> ###### 커스텀 하기

#### 회원탈퇴

#### 회원정보 수정

- User를 Update 하는 것. Userchangeform

#### 비밀번호 변경

## View decorators

> ###### 데코레이터(Decorator)

- django는 다양한 HTTP 기능을 지원하기 위해 view 함수에 적용할 수 있는 여러 데코레이터를 제공
  동작 예시-

#### Allowed HTTP methods

- django.views.decorators.http의 데코레이터를 사용하여 요청 메서드를 기반으로 접근을 제한할 수 있다.
- 일치하지 않는 메서드 요청이라면 405 Method Not Allowed를 반환
  - 요청 방법이 서버에게 전달 되었으나 사용 불가능한 상태
- 메서드 목록
  - 1.  require_http_methods()
  - 2.  require_POST()
  - 3.  require_safe()

> ###### require_http_methods()

- View 함수가 특정한 요청 method만 허용하도록 하는 데코레이터

> ###### require_POST()

> ###### require_safe()

## Limiting access to logged-in users

- 로그인 사용자에 대한 접근 제한하기
- is_authenticated attribute
  > ###### is_authenticated
- User model의 속성(attributes)중 하나
- 사용자가 인증 되었는지 여부를 알 수 있는 방법
- ## 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성
  -
- % 권한()과는 관련이 없으며, 사용자가 활성화 상태()이거나 유효한 세션()을 가지고 있는지도 확인하지 않음
