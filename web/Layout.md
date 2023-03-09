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
  - justify-content()
  - 