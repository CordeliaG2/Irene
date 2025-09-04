import math
import time
import random
from turtle import *

# -----------------------------
# Configuración inicial
# -----------------------------
bgcolor('black')
pensize(2)
tracer(10)
colores = ['white', '#ffcb7d', '#FFA216']  # colores originales

# Tortugas auxiliares
text_turtle = Turtle(); text_turtle.hideturtle(); text_turtle.penup()
star_turtle = Turtle(); star_turtle.hideturtle(); star_turtle.penup(); star_turtle.speed(0)
center_turtle = Turtle(); center_turtle.hideturtle(); center_turtle.penup(); center_turtle.speed(0)
halo_turtle = Turtle(); halo_turtle.hideturtle(); halo_turtle.speed(0); halo_turtle.penup()
stem_turtle = Turtle(); stem_turtle.hideturtle(); stem_turtle.speed(0); stem_turtle.color("green"); stem_turtle.pensize(6)

# -----------------------------
# Función para pétalos
# -----------------------------
def dibujo(a, n):
    circle(5 + n, 60)
    left(a)
    circle(5 + n, 60)

# -----------------------------
# Estrellitas
# -----------------------------
def draw_stars():
    star_turtle.clear()
    for _ in range(20):
        x = random.randint(-300, 300)
        y = random.randint(-100, 300)
        star_turtle.goto(x, y)
        star_turtle.dot(random.randint(2, 5), random.choice(["white", "#FFD700", "#87CEFA"]))

# -----------------------------
# Centro brillante
# -----------------------------
def draw_center_glow(size):
    center_turtle.clear()
    center_turtle.goto(0, 0)
    center_turtle.dot(int(size), "#FFD700")

# -----------------------------
# Halo brillante (fijo como fondo)
# -----------------------------
def draw_halo():
    halo_turtle.color("#FFD700")
    halo_turtle.pensize(1)
    for r in range(150, 300, 74):  # grande
        halo_turtle.penup()
        halo_turtle.goto(0, -r)
        halo_turtle.setheading(0)
        halo_turtle.pendown()
        halo_turtle.circle(r)
        halo_turtle.penup()

# -----------------------------
# Tallo centrado con animación de crecimiento
# -----------------------------
def draw_stem():
    stem_turtle.penup()
    stem_turtle.goto(0, 0)
    stem_turtle.setheading(-90)
    stem_turtle.pendown()
    for _ in range(20):
        stem_turtle.forward(10)
        update()
        time.sleep(0.05)

# -----------------------------
# Texto con sombra
# -----------------------------
def draw_text(msg):
    text_turtle.clear()
    # sombra
    text_turtle.goto(-1, 199)
    text_turtle.color("black")
    text_turtle.write(msg, align="center", font=("Arial", 18, "bold"))
    # texto principal
    text_turtle.goto(0, 200)
    text_turtle.color("#FFA216")
    text_turtle.write(msg, align="center", font=("Arial", 18, "bold"))

# -----------------------------
# Dibujar primero halo y tallo
# -----------------------------
draw_halo()
draw_stem()
j=1
# -----------------------------
# Animación con cambio de texto
# -----------------------------
for frame in range(400):
    base_size = 100
    oscillation = math.sin(frame * 0.05)
    current_size = base_size + base_size * 0.5 * oscillation

    # Brillo en el centro
    draw_center_glow(25 + 8 * oscillation)

    # Flor animada
    for i in range(180):
        # Estrellas parpadeantes
        if i % 20 == 0:
            draw_stars()

        # Texto en fases
            if i < 100 and j < 2:
                msg = "🌻 Para ti"
            elif i < 200 and j < 2:
                msg = "✨ Con cariño ✨"
            else:
                msg = "❤️ Eres especial ❤️"
            draw_text(msg)

        color_index = (i // 15) % 3
        c = colores[color_index]
        color(c, 'black')
        begin_fill()
        dibujo(90, current_size * i / 180)
        end_fill()
        dibujo(160, current_size * i / 180 * 1.2)
        penup()
        dibujo(0, 0)
        dibujo(90, current_size * i / 180)
        pendown()

    # Reset posición
    penup()
    home()
    pendown()
    j=3
    update()

done()

