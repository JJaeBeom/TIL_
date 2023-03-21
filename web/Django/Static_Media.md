# 20230321

## Django Form
앱 폴더 -> forms.py 생성 -> Class ArticleForm 선언
form은 model field와 달리 TextField 존재 x

> Form rendering options

- label & input 쌍에 대한 3가지 출력 옵션
1. as_p() #웬만하면 이거만
각 필드가 단락(p태그)로 감싸져서 렌더링 됨
2. as_ul()
각 필드가 목록 항목(li 태그)로 감싸져서 렌더링
ul 태그는 직접 작성해야함
3. as_table()
각 필드가 테이블(tr 태그)로 감까져서 렌더링
table태그는 직접 작성해야함

> Django의 HTML input 요소 표현 2가지
1. Form fields
input에 대한 유효성 검사 로직을 처리하며 템플릿에서 직접 사용됨

2. Widgets
웹페이지의 HTML input요소 렌더링을 담당
GET/POST 딕셔너리에서 데이터 추출
widgets는 반드시 Form fields에 할당됨
```
content = forms.CharField(widget=forms.Textarea)
```

#### Widgets
- Django HTML input element 표현, HTML렌더링 처리
- Form Fields와 구분 필요함
- Widgets는 유효성검사 X input element의 단순 raw한 렌더링처리


## Django Model Form
Model과 중복되는 부분이 많다. 
ModelForm을 사용하면 Form을 더 쉽게 작성 가능


## Static & Media Files