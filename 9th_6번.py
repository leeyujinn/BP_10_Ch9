# 6. 색상을 리스트에 저장한다. 리스트에 저장된 색상을 하나씩 꺼내어 거북이의 색상으로 설정하면서 속이 채워진 별을 랜덤한 위치에 그리는 프로그램을 작성해보자.
import turtle  # turtle 라이브러리 불러오기
import random  # random 라이브러리 불러오기

t = turtle.Turtle()  # 변수 t에 turtle.Turtle()를 선언
s = turtle.Screen()  # 변수 s에 turtle.Screen()을 선언
s.bgcolor("black")  # 배경을 검은색으로 지정


def draw_star(aturtle, colour, side_length, x, y):  # draw_star로 함수를 선언
    aturtle.color(colour)  # 색을 변수 colour로 지정
    aturtle.begin_fill()  # 도형을 색칠할 준비
    aturtle.penup()  # 펜 올리기
    aturtle.goto(x, y)  # (x,y)로 이동
    aturtle.pendown()  # 펜 내리기
    for i in range(5):  # 변수 i를 5번 반복
        aturtle.forward(side_length)  # 앞으로 변수 side_length만큼 전진
        aturtle.right(144)  # 오른쪽으로 144도 회전
        aturtle.forward(side_length)  # 앞으로 변수 side_length만큼 전진
    aturtle.end_fill()  # 그린 도형에 색칠하기


for i in range(20):  # 변수 i를 20만큼 반복
    # 변수 color에 흰색,노란색,파란색,하늘색,주황색,초록색 중 랜덤하게 지정
    color = random.choice(
        ['white', 'yellow', 'blue', 'skyblue', 'orange', 'green'])
    # 10부터 100까지의 숫자가 랜덤으로 지정되며 변수 side_length에 저장
    side_length = random.randint(10, 100)
    x = random.randint(-200, 200)  # -200부터 200까지의 숫자가 랜덤으로 지정되며 변수 x에 저장
    y = random.randint(-200, 200)  # -200부터 200까지의 숫자가 랜덤으로 지정되며 변수 y에 저장
    draw_star(t, color, side_length, x, y)  # draw_star 함수의 결과값을 출력

t._screen.exitonclick()  # 마우스로 클릭해야 화면이 종료됨
