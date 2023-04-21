# 20230417

## Django REST framework(Single Model) - POST

#### Build RESTful API - Article

> POST(1/4)

- 게시글 데이터 생성하기
  
  created는 post다
  POST는 생성!
  받은 데이터를 유효성검사하고 저장하고 Response로 JSON형태로 반환해주면 끝. 
  
  JSON데이터, status정보를 넣어준다. 
  기억이 안나면 모델 폼을 serializer로 바꾸는걸 생각해보자
  
                                                                  사용자입력
  
  serializer = ArticleSerializer(<u>data=request.data</u>)
  if serializer.is_valid(): 유효성 검사
  
      serializer.save()
  
      return Response(<u>serializer.data</u>, status=status.HTTP_201_CREATED)
  
                                      저장된 데이터                                생성은 201

> ###### DETAIL

Detail.
pk가 주소에 포함. variable routing
path
def (pk정보)
  데이터 참고
  serializer(data)
  return Response(serialize data)

get_object_or_404 << get()과 같다. 있으면 하나 찾아오고 없으면 404 리턴
get_list_or_404 < all() 데이터가 하나라도 없으면 404 리턴, 싹다 있으면.

is_valid()에 raise_exception=True 인자 사용가능

DELETE < 게시글 1개를 삭제하는 거니까, 게시글 1개를 나타내는 article_pk가 필요. 자연스럽게 delete 위치는, article_detail에서 작성
GET일 때는 조회 << 
DELETE 일때는 삭제 << 작성하는법 이해하기
return Response(status=status.HTTP_204_NO_CONTENT)   삭제는 204 
Response 첫번째 인자에, 딕셔너리 형태로 (삭제된 pk정보라던지) 메세지로 전달 가능.
return Response({'pk':article_pk}, status=status.HTTP_204_NO_CONTENT) 

<u>생성은 201, 삭제는 204</u>

> ###### UPDATE

CREATE와 UPDATE는 한끗차이.
CREATE에서는 그냥 데이터를 받아왔었다면, UPDATE에서는 기존 정보를 추가하는것,
serializer = ArticleSerializer(<u>article</u>, data=request.data)

## Django REST framework(N:1)

큰 흐름 자체는 싱글모델과 동일.
차이점으로, 

article과 comment가 1:N관계. article이 1, comment가 N
ForeignKey는 N인 곳에 정의.
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

###### 전체 댓글 불러오는 법

=> article 전체 정보를 가져오는것과 같다. 모든걸 가져오고 그걸 serializer로 변환
all() 0개 이상인것만 many=True

###### 단일 댓글 조회 << 1개 조회

article detail과 같다. 데이터 1개 찾아오고, 데이터 찾고,
serializer로 변환. 그 변환된 데이터를 응답. comment냐 article이냐 차이.

READ부분은 싱글모델과 동일하다.

###### 단일 댓글 데이터 생성하기.

CREATE - 싱글모델과 조금 다른 부분이 존재.
단독으로 생성되는 것이 아니라, 어떤 게시글인지.
즉, 게시글 정보도 같이 저장이 되어야 한다.
URL에 article_pk도 전달됨.
싱글 모델과의 차이점. 
찾을 때, pk=article_pk
save할때, article=article

```python
 @api_view(['POST'])    
 def comment_create(request, article_pk):
     article = Article.objects.get(pk=article_pk)
     serializer = CommentSerializer(data=request.data)
     if serializer.is_valid(raise_exception=True):
         serializer.save(article=article)
         return Response(serializer.data, status=status.HTTP_201_CREATED)
```

유효성검사에서. article field 데이터 또한 사용자로부터 입력 받도록 설정되어있어서 아래같은 오류가 뜸
'article' : ["This field is required."]
읽기 전용(Read only)으로 설정해주면 검사를 하지 않음
read_only_fields = ('article',)

달라진점. 댓글생성이 싱글모델과

1. 게시글 찾기
2. 저장할 때 게시글도 같이 저장
3. read_only 설정

###### DELETE & PUT

싱글모델과 거의 동일

PUT 저장할 때(save할때) article 정보를 안넣어줘도 됨.
이미 comment에 article정보가 저장되어 있기 때문.

```python
@api_view(['GET'])    
def comment_detail(request, comment_pk):
    if request.method == 'GET':
        comment = Comment.objects.get(pk=comment_pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
```

#### N:1 역참조 데이터 조회

33

- 특정 게시글에 작성된 댓글 목록 출력하기
  
  - 기존 필드 override
    
    <!-- - fields = ['id','title','comment)set',] -->
  
  역참조명 변경한다면, 변경된 이름(related_name)으로 serializer에서 override 해줘야 함
  역참조는 역참조 명을 따른다.
  
  게시글과 댓글은 1:N이라, many=True 설정이 필수. 역참조는 사용자가 입력할 필요가 없기에, read_only=True 설정을 해줌
  
  참조된 대상은 참조하는 대상의 표현에 포함되거나, 중첩(nested)될 수 있음
  
  **두 클래스의 상/하 위치를 변경해야함**

- 특정 게시글에 작성된 댓글의 개수 출력하기
  
  - 새로운 필드 추가하는 방법
    - 내부에서 사용되는 정보를 가지고, 새로운 필드를 만들 수 있다. ex)게시글 조회시 해당 게시글 댓글 개수까지 함께 출력

```python
class ArticleListSerializer(serializers.ModelSerializer):
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
```

- source는 self argument가 

- override 하는 것들은 직접 read_only=True 속성을 설정/

- 밑에 작성하는 read_only_fields 는 Article의 기본 필드만 적용/ override 된건 적용 x

```python
article = Article.objects.get(pk=article_pk)
comment = Comment.objects.get(pk=comment_pk)
# <!-- ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ -->
# 적용 후, 이전에는 500 상태코드, 후에는 404 상태코드 응
article = get_object_or_404(Article, pk=article_pk)
comment = get_object_or_404(Comment, pk=comment_pk)
```

## Serializer 활용하기

to_representation() 

## 문서화
