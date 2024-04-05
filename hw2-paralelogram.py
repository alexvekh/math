import plotly.graph_objects as go
import numpy as np
from numpy import linalg as LA

m0 = np.array([0, 0, 0])
m1 = np.array([2, 1, 0])
m2 = np.array([0, 3, 1])
m3 = np.array([1/2, 1/2, 1])

a = m1 - m0
b = m2 - m0
c = m3 - m0

# Знайдемо координати інших вершин паралелепіпеда, враховуючи рівність координат векторів, що утворюють протилежні грані,
# оскільки в паралелепіпеда протилежні грані паралельні і рівні, отже вектори, що їх утворюють колінеарні і мають рівні модулі
m4 = m0 + a + b
m5 = m0 + a + c
m6 = m0 + b + c
m7 = m0 + a + b + c


#Візуілізуємо вершини
vertices = np.array([m0, m1, m2, m3, m4, m5, m6, m7])
fig = go.Figure()
fig.add_trace(go.Scatter3d(
    x=vertices[:, 0], y=vertices[:, 1], z=vertices[:, 2],
    mode='markers+text',
    marker=dict(
        size=5,
        color='palevioletred'),
    text=['m0', 'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7'],
    textposition="bottom center",
    showlegend=False
))


#Візуілізуємо вектори a,b,c із підписами
edges_solid = [m1,m2,m3]
for i, edge in enumerate(edges_solid):
    fig.add_trace(go.Scatter3d(
        x=[m0[0], edge[0]], y=[m0[1], edge[1]], z=[m0[2],edge[2]],
        mode='lines',
        line=dict(color='maroon', width=3),
        showlegend=False
    ))

    mid_point = edge / 2
    fig.add_trace(go.Scatter3d(
        x=[mid_point[0]], y=[mid_point[1]], z=[mid_point[2]],
        text=['a', 'b', 'c'][i],
        mode='text',
        showlegend=False
    ))


#Додамо конуси-напрямки векторів
for i, edge in enumerate(edges_solid):
    fig.add_trace(go.Cone(
        x=[edge[0]*0.95], y=[edge[1]*0.95], z=[edge[2]*0.95],
        u=[edge[0]], v=[edge[1]], w=[edge[2]],
        sizemode="absolute",
        sizeref=0.1,
        showscale=False
    ))


#Додамо вектори-ребра паралелепіпеда, що не були задані за умовою
edges_dotted = [
    [m1, m4],
    [m1, m5],
    [m2, m4],
    [m2, m6],
    [m3, m5],
    [m3, m6],
    [m4, m7],
    [m5, m7],
    [m6, m7]
]

for edge in edges_dotted:
    edge_points = np.array(edge)
    fig.add_trace(go.Scatter3d(
        x=edge_points[:, 0], y=edge_points[:, 1], z=edge_points[:, 2],
        mode='lines',
        line=dict(color='darkolivegreen', width=3, dash='dash'),
        showlegend=False
    ))


#Назви вісей координат
fig.update_layout(scene = dict(
                    xaxis_title='Вісь X',
                    yaxis_title='Вісь Y',
                    zaxis_title='Вісь Z'))

#Розфарбуємо фон
fig.update_layout(scene = dict(
                    xaxis = dict(
                         backgroundcolor="rgb(200, 200, 230)",
                         gridcolor="white",
                         showbackground=True,
                         zerolinecolor="white",),
                    yaxis = dict(
                        backgroundcolor="rgb(230, 200,220)",
                        gridcolor="white",
                        showbackground=True,
                        zerolinecolor="white"),
                    zaxis = dict(
                        backgroundcolor="rgb(240, 230,200)",
                        gridcolor="white",
                        showbackground=True,
                        zerolinecolor="white",),),
                    width=800,
                    margin=dict(
                    r=10, l=10,
                    b=10, t=10))


fig.update_layout(title='Візуалізація вершин паралелепіпеда', autosize=True,
                  width=800, height=800,
                  margin=dict(l=65, r=50, b=65, t=90))

fig.show()