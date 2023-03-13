# 20230310

## Bootstrap

> 

> CDN
>   Content Delivery(Distribution) Network

- 컨텐츠(CSS, JS, Image, Text 등)를 효율적으로 전달하기 위해 여러 노드를 가진 네트워크에서 데이터를 제공하는 시스템

개별 end-user의 가까운 서버를 통해 빠르게 전달 가능(지리적 이점)
외부 서버를 활용함으로써 본인 서버의 부하가 적어짐

> spacing

**단위** - **px**, **%**

**vw** - V: Viewport Width
**vh** - V: Viewport height
  100VW = Viewport의 100%
**rem** - 상대적인 단위
  <HTML> 폰트 사이즈에 비례하게 작동
    기본적으로 아무것도 안한 사이즈는 16px
    10rem = 160px    0.5rem = 8px

.mx-0 << x
  x - for classes that set both *-left and *-right
.my-0 << y
  y - for classes that set both *-top and *-bottom

> 반응형 웹(Responsive Web)
>  부트스트랩 쓰는 가장 큰 이유 중 하나
>  같은 컨텐츠를 보는 각기 다른 디바이스
>  Responsive Web Design

- 다양한 화면 크기를 가진 디바이스들이 등장함에 따라 responsive web design 개념이 등장
- 반응형 웹은 별도의 기술 이름이 아닌 웹 디자인에 대한 접근 방식, 반응형 레이아웃 작성에 도움이되는 사례들의 모음 등을 기술하는데 사용되는 용어
- 예시
  - Media Queries, Flexbox, Bootstrap Grid System, The wiewport meta tag

#### The Grid System

- CSS가 아닌 편집 디자인에서 나온 개념으로 구성 요소를 잘 배치해서 시각적으로 좋은 결과물을 만들기 위함
- 기본적으로 안쪽에 있는 요소들의 오와 열을 맞추는 것에서 기인
- 정보 구조와 배열을 체계적으로 작성하여 정보의 질서를 부여하는 시스템

12개 column 고정
6개의 grid breakpoints