import turtle
import colorsys
#importei a livraria turtle e importei a color dela, assim eu defini a função de cada linha além das cores que seriam usadas no desenho
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
n = 10
h = 0
#defini a força e potencia de velocidade na qual o desenho seria feito, e criei uma tarefa repetitiva que não se finaliza logo o usuario a deixe

for i in range(999):
    c=colorsys.hsv_to_rgb(h,1,0.9)
    h+=1/n
    t.color(c)
    t.left(145)
    for j in range(5):
        t.forward(300)
        t.left(150)
        