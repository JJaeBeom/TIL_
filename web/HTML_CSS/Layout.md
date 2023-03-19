# 20230309

## Float

> Css 원칙 1. 기억하나
> 모든 요소는 네모(박스모델)이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다.(좌측 상단에 배치)
> 그럼 다른 배치는?
> Float

- 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인요소들이 주변을 wrapping하도록 함

- 요소가 Normal flow를 벗어나도록 함
  
  > Float 속성

- none: 기본값

- left: 요소를 왼쪽으로 띄움

- right: 요소를 오른쪽으로 띄움
  
  > Float 정리

- Float는 레이아웃을 구성하기 위해 필수적으로 활용 되었으나, 최근 Flexbox, Grid 등장과 함께 사용도가 낮아짐

- Float 활용 전략 - Normal Flow에서 벗어난 레이아웃 구성
  
  - 원하는 요소들을 Float로 지정하여 배치

## Flexbox

> layout을 위해 탄생한 Flexbox

- Float& inline-block 등을 이용한 layout은 솔직히 사용하기 힘듬

- layout에 특화된 기능.
  
  > CSS Flexible Box Layout

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델

- 축
  
  - main axis(메인 축)
  - cross axis(교차 축)

- 구성요소
  
  - Flex Container(부모요소)
  - Flex Item(자식요소)

> Flexbox 축

> Flexbox 구성요소

- Flex Container(부모 요소)
  - flexbox 레이아웃을 형성하는 가장 기본적인 모델
  - Flex item들이 놓여있는 영역
  - display 속성을 flex 혹은 inline-flex로 지정
- Flex Item(자식 요소)
  - 컨테이너에 속해 있는 컨텐츠(박스)

> Flexbox 시작
> .flex-container{
>     display: flex;
> }
> 부모 요소에 display:flex

> Flex 속성

- 배치 설정
  - flex-direction
  - flex-wrap
- 공간 나누기
  - justify-content(main axis)
  - align-self(cross axis)

- 정렬
  - align-items(모든 아이템을 cross axis 기준으로)
  - aling-self(개별 아이템)

> Flex 속성: flex-direction
- Main axis 기준 방향 설정
1) row  - 가로
2) row-reverse - 가로 (오른쪽에서 부터)
3) column - 세로
4) column-reverse - 세로(밑에서부터 위로)

> Flex 속성: flex-wrap
- 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정
- 즉, 기본적으로 컨테이너 영역을 벗어나지 않도록 함
1) wrap - 줄넘김(넘치면 그 다음 줄로 배치)
2) nowrap - 쫙(한줄에 배치)

> flex-flow 
- flex-direction과 flex-wrap의 shorthand
- ex) flex-flow : row nowrap;

> Flex 속성: justify-content & align-content
- 공간 배분
 - flex-start
 - flex-end: 아이템들을 끝 쪽으로
 - center: 중앙으로
 - space-between: 아이템 사이의 간격을 균일하게 분배
 - space-around: 아이템을 둘러싼 영역을 균일하게 분배(가질 수 있는 영역을 반으로 나눠서 양쪽에)

> Flex 기타 속성
- order: 배치순서
- flex-grow: 남은 영역을 아이템에 분배
