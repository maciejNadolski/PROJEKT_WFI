from vpython import *
import tkinter as tk


def animation(m1, m2, k1, k2, k3, period, x1):
    scene = canvas(title='Wizualizacja', width=1200, height=400)

    box1 = sphere(pos=vector(-0.5, 0, 0), radius=0.2, color=color.blue)
    box2 = sphere(pos=vector(0.5, 0, 0), radius=0.2, color=color.red)
    wall_left = box(pos=vector(-2, 0, 0), size=vector(0.1, 2, 2), color=color.green)
    wall_right = box(pos=vector(2, 0, 0), size=vector(0.1, 2, 2), color=color.green)
    spring1 = helix(pos=wall_left.pos, axis=box1.pos - wall_left.pos, radius=0.1, coils=5, thickness=0.05,
                    color=color.orange)
    spring2 = helix(pos=box1.pos, axis=box2.pos - box1.pos, radius=0.1, coils=5, thickness=0.05, color=color.orange)
    spring3 = helix(pos=box2.pos, axis=wall_right.pos - box2.pos, radius=0.1, coils=5, thickness=0.05,
                    color=color.orange)

    g1 = graph(xtitle="t [s]", ytitle="x [m]", width=1200, height=500, xmax=period, ymax=5, ymin=-0.05)

    f1 = gcurve(color=color.blue, dot=True)
    f2 = gcurve(color=color.red, dot=True)

    x2 = 0
    v1 = 0
    v2 = 0
    t = 0
    dt = 0.01

    while t < period:
        rate(300)
        a1 = (-k1 * x1 - k2 * (x1 - x2)) / m1
        a2 = (-k3 * x2 - k2 * (x2 - x1)) / m2
        v1 = v1 + a1 * dt
        v2 = v2 + a2 * dt
        x1 = x1 + v1 * dt
        x2 = x2 + v2 * dt
        t = t + dt

        box1.pos.x = x1 - 0.5
        box2.pos.x = x2 + 0.5

        f1.plot(t, -x1 + 2.5)
        f2.plot(t, -x2 + 1.5)

        spring1.pos = wall_left.pos
        spring1.axis = box1.pos - wall_left.pos
        spring2.pos = box1.pos
        spring2.axis = box2.pos - box1.pos
        spring3.pos = box2.pos
        spring3.axis = wall_right.pos - box2.pos


def gui():
    root = tk.Tk()
    root.title("Parametry")
    root.geometry("500x600")

    label = tk.Label(root, text="Podaj parametry", font=30)
    label.pack()

    k1Scale = tk.Scale(root, from_=1, to=10, resolution=0.1, orient=tk.HORIZONTAL, label='Stała k1')
    k1Scale.pack()

    m1Scale = tk.Scale(root, from_=0.1, to=10, resolution=0.1, orient=tk.HORIZONTAL, label='Masa Niebieskego')
    m1Scale.pack()

    k2Scale = tk.Scale(root, from_=1, to=10, resolution=0.1, orient=tk.HORIZONTAL, label='Stała k2')
    k2Scale.pack()

    m2Scale = tk.Scale(root, from_=0.1, to=10, resolution=0.1, orient=tk.HORIZONTAL, label='Masa Czerwonego')
    m2Scale.pack()

    k3Scale = tk.Scale(root, from_=1, to=10, resolution=0.1, orient=tk.HORIZONTAL, label='Stała k3')
    k3Scale.pack()

    tScale = tk.Scale(root, from_=5, to=360, resolution=1, orient=tk.HORIZONTAL, label='Czas')
    tScale.pack()

    x1Scale = tk.Scale(root, from_=0.1, to=1, resolution=0.1, orient=tk.HORIZONTAL, label='Przesunięcie')
    x1Scale.pack()

    actionButton = tk.Button(root, text="Rysuj", width=10,
                             command=lambda: animation(m1Scale.get(), m2Scale.get(), k1Scale.get(), k2Scale.get(),
                                                       k3Scale.get(), tScale.get(), x1Scale.get()))
    actionButton.pack()
    root.mainloop()


if __name__ == "__main__":
    gui()
