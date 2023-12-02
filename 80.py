from re import A
import turtle as t
t.color("blue")
t.bgcolor("black")
t.shape("turtle")
for i in range (10):
    for colors in ["blue", "red", "dark violet", "green","yellow","white"]:
        t.color(colors)
        t.speed(100)
        t.forward(10)
        t.left(11)
        t.circle(123)
t.done()