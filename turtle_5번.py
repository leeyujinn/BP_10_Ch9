# 5. 색상을 리스트에 저장한다. 리스트에 저장된 색상을 하나씩 꺼내어 거북이의 색상으로 설정하면서 속이 채워진 다각형을 그리는 프로그램을 작성해보자.
import turtle  # turtle 라이브러리 불러오기
import random  # random 라이브러리 불러오기

t = turtle.Turtle()  # 변수 t에 turtle.Turtle()를 선언
s = turtle.Screen()  # 변수 s에 turtle.Screen()을 선언


def draw_shape(t, c, length, sides, x, y):  # draw_shape로 함수를 선언
    t.up()  # 펜 올리기
    t.goto(x, y)  # (x,y)로 이동
    t.down()  # 펜 내리기
    t.fillcolor(c)  # 변수 c의 색깔로 색을 채우기
    angle = 360.0 / sides  # 360.0/sides를 변수 angle로 선언
    t.begin_fill()  # 도형을 색칠할 준비
    for dist in range(sides):  # 변수 dist에 변수 sides만큼 반복
        t.forward(length)  # 앞으로 length만큼 전진
        t.left(angle)  # 왼쪽으로 angle도 회전
    t.end_fill()  # 그린 도형에 색칠하기


for i in range(10):  # 변수 i를 10번 반복
    # 변수 color에 흰색,노란색,파란색,하늘색,주황색,초록색 중 랜덤하게 지정됨
    color = random.choice(
        ['white', 'yellow', 'blue', 'skyblue', 'orange', 'green'])
    # 10부터 100까지의 숫자가 랜덤으로 지정되며 변수 side_length에 저장
    side_length = random.randint(10, 100)
    sides = random.randint(3, 10)  # 3부터 10까지의 숫자가 랜덤으로 지정되며 변수 sides에 저장
    x = random.randint(-200, 200)  # -200부터 200까지의 숫자가 랜덤으로 지정되며 변수 x에 저장
    y = random.randint(-200, 200)  # -200부터 200까지의 숫자가 랜덤으로 지정되며 변수 y에 저장
    draw_shape(t, color, side_length, sides, x, y)  # draw_shape 함수의 결과값을 출력

t._screen.exitonclick()  # 마우스로 클릭해야 화면이 종료됨
