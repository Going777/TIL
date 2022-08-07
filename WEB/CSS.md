# CSS (Cascading Style Sheets)

HTML 태그를(원하는 부분을) **선택하고**, **스타일을 지정**하기 위한 언어  

`DOM Tree`구조로 구조화된 요소에서 상위요소에 스타일을 입히면 하위요소에도 연쇄적으로 적용된다 

```css
# 모든 h1 태그에 적용할 스타일 설정
h1 { # 선택자 
	color: blue; # 글자색 (스타일 지정)
	font-size: 15px; # 글자 크기 (스타일 지정)
}
```

### CSS 정의 방법

1. 인라인(inline) - 시작 태그에 직접 style 속성을 작성 / 각각의 스타일은 세미콜론(;)로 구분 / width, height를 주면 에러는 안나지만 스타일 적용은 안됨

```html
<h1 style="color: blue; font-size: 100px;">Hello</H1>
```

1. 내부참조(embedding) - .html 파일에서 <head>태그 내에 <style>에 지정

```html
<head>
	<style>
		h1 {                # 선택자 자리
			color: blue;      # : ; 빼먹지 않게 주의
			font-size: 40px
		}
	</style>
</head>
```

1. 외부참조(link file) - 외부 CSS 파일을 <head>내 <link>를 통해 불러옴

```html
# mystyle.css 파일
p { 
	color: pink; 
	font-size: 25px; 
} 

# 원래 .html 파일의 <head> 태그 내에서 작성
<head>
	<link rel="stylesheet" href="mystyle.css">
</head>
```

### CSS Selectors (선택자)

[ 기본 선택자 ] ⭐

- 전체 선택자 `* {}`, 요소 선택자 `tag명 {}`
- 클래스 선택자 `.class명 {}`, 아이디 선택자 `#id명 {}`, 속성 선택자 `button[type=”submit”] {}`

[ 결합자 (Combinators) ] ⭐

- 자손 결합자(A `공백` B) : A의 자식요소 중 **모든** B 요소
- 자식 결합자(A `>` B) : A의 자식요소 중 **바로 밑 레벨의 모든** B 요소 (일촌자식)
- 일반 형제 결합자(A `~` B) : A의 형제 요소 중 뒤에 위치하는 **모든** B 요소
- 인접 형제 결합자(A `+` B) : A의 형제 요소 중 **바로 뒤**에 위치하는 B 요소 **하나**

[ 의사 클래스/요소 (Pseudo Class) ]

- 링크, 동적 의사 클래스
- 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자
- A`:first-child` : A 요소에 해당하는 첫 번째 요소
- A`:last-child` : A 요소에 해당하는 마지막 번째 요소
- A`:not(:first-child)` : A 요소에 해당하지 않는 첫 번째 요소
- A`:nth-child(n)` : A요소 중 n번째 요소 (odd, even, #, #n, #n+#과 같이 식을 넣어서 찾을 수도 있음)

### CSS 적용 우선순위 (cascading order)

- 범위가 좁을수록/구체적일수록 강하다!!
- 같은 레벨의 선택자라면 **뒤에 작성된 코드의 우선순위가 높다**

```java
**!important >** **인라인 > id > class > 요소(tag) > 전체(*)**
```

### CSS 상속

- CSS는 상속을 통해 부모 요소의 속성이 자식에게 상속된다 / 상속이 되지 않는 요소도 존재한다
- 상속 되는 것
    - **Text 관련 요쇼** (`font`, `color`, `text-align`), `opacity`, `visibility`
- 상속 되지 않는 것
    - **Box model 관련 요소**(`width`, `height`, `margin`, `padding`, `border`, `box-sizing`, `display`)
    - **위치 관련 요소**(`position`, `top/right/bottom/left`, `z-index`)
- MDN 문서에서 확인 가능

### CSS 기본 스타일

- 크기 단위 - 브라우저 크기를 변경해도 고정적인 사이즈
    - `px` (픽셀) - 픽셀의 크기는 변하지 않기 때문에 **고정적인 단위** (픽셀 수가 올라갈수록 화질이 선명)
    - `%` - 백분율 단위로 **가변적인 레이아웃**에서 자주 사용
    - `em` -  **바로 위, 부모 요소에 지정된 사이즈에 상대적인 사이즈**를 가짐 (**상속의 영향을 받음)**
    - `rem` ⭐ - **최상위 요소(html)의 사이즈를 기준으로 배수 단위**를 가짐 
    ( 기본 브라우저 폰트 사이즈 = 16px )
    
    ```html
    <head>
    .font_big {
    	font_size: 36px;
    }
    .em {
    	font_size: 2em;
    }
    .rem {
    	font_size: 2rem;
    }
    </head>
    <body>
    	<ul class="font-big">
    		<li class="em">em</li>   # 36*2 = 72px
    		<li class="rem">rem</li> # 16*2 = 32px
    		<li>No class</li>        # 36px
    </body>
    ```
    
    ---
    
- 크기 단위(viewport) - 디바이스의 viewport(실제로 보고 있는 화면)를 기준으로 상대적인 사이즈가 결정됨 / 브라우저 크기에 따라 사이즈가 결정됨
    - `vw` ←현재 보고 있는 디바이스의 너비 크기의 1/100 단위 픽셀
    - `vh` ←현재 보고 있는 디바이스의 높이 크기의 1/100 단위 픽셀
    - `vmin` ← 최소값
    - `vmax` ← 최대값
- 색상 단위
    - `색상 키워드` ⭐ - 대소문자 구분 안함 / red, blue, black과 같이 특정 색을 직접 글자로 작성
    - `RGB 색상` ⭐ - 16진수 표기법 혹은 함수형 표기법을 사용해 특정 색을 표현 (0~255)
    `RGBA` - RGB + Alpha
    - `HSL 색상` - 색상, 채도, 명도를 통해 특정 색을 표현

### CSS Box Model  ⇒ 좌측 상단을 기준으로 정렬
💡 모든 요소는 네모(박스 모델)이고, 위에서부터 아래로(block), 왼쪽에서 오른쪽으로(inline) 쌓인다 (Normal Flow)
- 모든 HTML 요소는 box 형태로 되어 있음
- 하나의 박스는 네 부분(영역)으로 이루어짐
    - `content` - 글이나 이미지 등 요소의 실제 내용
    - `padding` - 테두리 안쪽의 내부 여백 **요소에 적용된 배경색, 이미지는 padding까지만 적용**됨 / 콘텐트와 테두리 간의 간격
    - `border` - 테두리 영역 (border-width/style/color)
    - `margin` - 테두리 바깥의 외부 여백 배경색을 지정할 수 없다 /  박스모델과 박스모델 간의 간격
    
    ![image](https://user-images.githubusercontent.com/109488657/183280377-d118bc3b-1b65-4a5c-8269-5b75995acee2.png)
    
    1. 모두 같은 값
    2. 상하 / 좌우 (십자가)
    3. 상 / 좌우 / 하 (나누기)
    4. 상 / 우 / 하 / 좌 (시계방향)
- 기본적으로 모든 요소의 box-sizing은 content-box
    - Padding을 제외한 순수 contents 영역만을 box로 지정
- 다만, 우리가 일반적으로 영역을 볼 때 border까지의 너비를 100px로 보는 것을 원함
    - 그 경우 box-sizing을 `border-box`로 지정

### CSS Display
💡 display에 따라 크기와 배치가 달라진다.
- `display: block`
    - 줄 바꿈이 일어나는 요소
    - 기본 너비는 가질 수 있는 너비의 100%인데, 만약 width를 부여했을 경우, 남는 공간은 margin으로 대체됨
    - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음
    - **div / ul, ol, li / p / hr / form** 등 ( 기본 너비는 가질 수 있는 너비의 100%, 차지할 수 있는 한 다 차지 )
- `display: inline`
    - 줄 바꿈이 일어나지 않는 행의 일부 요소
    - content 너비만큼 가로 폭을 차지한다
    - **width, height, margin-top, margin-bottom을 지정할 수 없다**
    - 상하여백은 line-heihgt로 지정한다
    - **span / a / img / input, label / b, em, i, strong** 등 ( 기본 너비는 컨텐츠 영역만큼 )
- `display: inline-block`
    - block과 inline 레벨 요소의 특징을 모두 가짐
    - inline처럼 한 줄에 표시할 수 있고, block처럼 width, height, margin 속성을 모두 지정할 수 있음
- `display: none` ⭐
    - 해당 요소를 화면에 표시하지 않고(생성 조차 안됨), 공간조차 부여되지 않음
    
    cf) visibility: hidden은 해당 요소가 공간은 차지하나(생성은 됨) 화면에 표시만 하지 않는다
    
### CSS Position
💡 position으로 위치의 기준을 변경한다. => relative, absolute, fixed, sticky
- [MDN Postion](https://developer.mozilla.org/ko/docs/Web/CSS/position)
- 요소의 위치를 지정
- `static` - 모든 태그의 기본 값(기준 위치) (**normal flow**를 따른다)
    - 일반적인 요소의 배치 순서에 따름(좌측 상단)
    - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨
- 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능
    - `relative`(상대 위치) - **원래 있던 자리(static)를 차지하고 있음**, 자기 자신의 static 위치를 기준으로 기존 위치로 이동 (**normal flow는 유지**)
    
    ![image](https://user-images.githubusercontent.com/109488657/183280400-215833e3-4e7d-4282-917c-a1882058de16.png)
    
    - `absolute`(절대 위치) - 상위 부모 요소의 자리를 기준으로 위치를 이동 / z-index를 이용하여 정렬을 바꿀 수 있음 (**normal flow 유지X**)
    - 
    
    ![image](https://user-images.githubusercontent.com/109488657/183280411-2431c483-e43f-40bf-902c-fed61225602b.png)
    
    - `sticky`(기본적으로 static이지만 스크롤에 따라 fixed로 변경) - 스크롤을 하더라도 처음 생성된 위치를 기준으로 고정되어 있음  (normal flow 유지X)
    - `fixed`(고정 위치) - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지 않음

### Float

- 박스나 사진을 왼쪽이나 오른쪽으로 이동시켜, 텍스트를 포함한 **인라인 요소들이 주변을 감싸도록** 하는 것
- 요소가 **Normal flow를 벗어나도록** 함
- `none` : 기본값
- `left` : 요소를 왼쪽으로 띄움
- `right` : 요소를 오른쪽으로 띄움

### Flex Box (Flexible Box Layout)

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
- 이전까지 Normal Flow를 벗어나기 위한 방법은 Position, Flat밖에 없었다
  > 수직정렬, 아이템 너비 혹은 간격을 동일하게 배치하는게 너무 어렵고 불편 > flex box 등장 
    
    ![image](https://user-images.githubusercontent.com/109488657/183281388-a99ac08b-719d-4679-8883-a4c210ad7534.png)
    
- 축 → **flex direction에 따라 메인축/교차축의 방향이 바뀐다**
    - main axis (메인 축)
    - cross axis (교차 축)
- 구성요소
    - Flex Containter (부모 요소) : container 내 item을 적용하고 싶다면  Container에 `display:flex or inline-flex;`를 적용해야 한다!!
    - Flex Item (자식 요소) : 컨테이너에 속해 있는 컨텐츠(박스)
- 배치 설정
    - `flex-direction` : 역방향의 경우 HTML 태그 선언 순서와 시각적으로 다르니 유의해야 함 (웹 접근성에 영향)
        - `row` , `row-reverse` , `column` , `column-reverse`
    
    ![image](https://user-images.githubusercontent.com/109488657/183281409-599b6540-74f5-4b2b-a103-72c04ea0945d.png)
    
    - `flex-wrap` : 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정
        - `wrap`: 기본 크기를 유지하되, 넘치면 그 다음 줄로 배치
        - `nowrap`(기본값): 기본 크기를 줄여 한 줄에 배치
        - `wrap-reverse`: 밑에서부터 좌에서 우로 쌓임 (최신글이 위에 오도록 하고 싶을 때)
    - `flex-flow: flex-direction flex-wrap` (축약형)
- 공간 나누기
    - `justify-content` (**main axis 기준**으로)
    - `align-content` (**cross axis 기준**으로 → 아이템이 한 줄로 배치되는 경우에는 확인 불가능)
        - `flex-start`(기본값): 아이템들을 axis 시작점으로
        - `flex-end`: 아이템들을 axis 끝 쪽으로 (순서 변경X)
        - `center`⭐: 아이템들을 axis 중앙으로
        - `space-between`⭐: 아이템 사이의 간격을 균일하게 분배 (양 끝단에 여백X)
        - `space-around`⭐: 아이템을 둘러싼 영역을 균일하게 분배 (실제비율=1:2:2:1) (양 끝단 여백 O)
        - `space-evenly`⭐: 모든 영역을 균일하게 분배 (양 끝단 여백 O)
        
        ![image](https://user-images.githubusercontent.com/109488657/183281430-ae3e406c-439c-438e-93dd-7641c64eb93d.png)
        
- 정렬
    - `align-items` (모든 아이템을 **cross axis 기준**으로 정렬)
    - `align-self` (개별 아이템을 **cross axis 기준**으로 정렬)
        - `strech`(기본값): 컨테이너를 가득 채움
        - `flex-start`: 위
        - `flex-end`: 아래
        - `center`: 가운데
        - `baseline`: 텍스트 baseline에 기준선을 맞춤

**⇒ 수평 수직 정렬 : `justify_contenr:center; align-items:center;`**

- 기타 속성
    - `flex-grow`: 남는 영역을 아이템에 분배
    - `order`: 배치 순서 변경
