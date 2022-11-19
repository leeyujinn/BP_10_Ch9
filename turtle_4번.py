# 4. 색상을 리스트에 저장한다. 리스트에 저장된 색상을 하나씩 꺼내어 거북이의 색상으로 설정하면서 속이 채워진 사각형을 그리는 프로그램을 작성해보자.
import turtle  # turtle 라이브러리 불러오기
import random  # random 라이브러리 불러오기
t = turtle.Turtle()  # 변수 t에 turtle.Turtle()를 선언
t.shape("turtle")  # turtle 도형 불러오기


def draw_square(x, y, c):  # draw_square로 함수를 선언
    t.up()  # 펜 올리기
    t.goto(x, y)  # (x,y)로 이동
    t.down()  # 펜 내리기
    t.color("black", c)  # 선은 검은색, 채우기는 변수 c로 지정
    t.begin_fill()  # 도형을 색칠할 준비
    t.forward(100)  # 앞으로 100만큼 전진
    t.left(90)  # 왼쪽으로 90도 회전
    t.forward(100)  # 앞으로 100만큼 전진
    t.left(90)  # 왼쪽으로 90도 회전
    t.forward(100)  # 앞으로 100만큼 전진
    t.left(90)  # 왼쪽으로 90도 회전
    t.forward(100)  # 앞으로 100만큼 전진
    t.left(90)  # 왼쪽으로 90도 회전
    t.end_fill()  # 그린 도형에 색칠하기


# 변수 c(채우기)를 노란색, 빨간색, 보라색, 파란색 순서대로 반복함
for c in ["yellow", "red", "purple", "blue"]:
    x = random.randint(-100, 100)  # -100부터 100까지의 숫자가 랜덤으로 지정되며 변수 x에 저장
    y = random.randint(-100, 100)  # -100부터 100까지의 숫자가 랜덤으로 지정되며 변수 y에 저장
    draw_square(x, y, c)  # draw_square 함수의 결과값을 출력

t._screen.exitonclick()  # 마우스로 클릭해야 화면이 종료됨
