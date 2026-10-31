# ROS2 Hardware Interface va 5-Darajali (Kvintik) Splayn Dinamikasi

## 1. 5-Darajali (Kvintik) Ko'phad Splayni (Quintic Polynomial)
Sanoat robotlarida harakatning boshlanishi va tugashida siltanishni (jerk) nolga tenglashtirish va reduktorlarni ortiqcha dinamik yuklamadan asrash uchun 5-darajali ko'phad qo'llaniladi:

$$s(t) = a_0 + a_1 t + a_2 t^2 + a_3 t^3 + a_4 t^4 + a_5 t^5$$

Tezlik va tezlanish:
$$\dot{s}(t) = a_1 + 2 a_2 t + 3 a_3 t^2 + 4 a_4 t^3 + 5 a_5 t^4$$
$$\ddot{s}(t) = 2 a_2 + 6 a_3 t + 12 a_4 t^2 + 20 a_5 t^3$$

### Chegaraviy shartlar ($t \in [0, T]$):
$$s(0) = q_0, \quad s(T) = q_1$$
$$\dot{s}(0) = v_0, \quad \dot{s}(T) = v_1$$
$$\ddot{s}(0) = a_0, \quad \ddot{s}(T) = a_1$$

Ushbu 6 ta tenglama yagona $6 \times 6$ chiziqli tenglamalar tizimiga keltiriladi:
$$\begin{bmatrix}
1 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 2 & 0 & 0 & 0 \\
1 & T & T^2 & T^3 & T^4 & T^5 \\
0 & 1 & 2T & 3T^2 & 4T^3 & 5T^4 \\
0 & 0 & 2 & 6T & 12T^2 & 20T^3
\end{bmatrix}
\begin{bmatrix} a_0 \\ a_1 \\ a_2 \\ a_3 \\ a_4 \\ a_5 \end{bmatrix}
=
\begin{bmatrix} q_0 \\ v_0 \\ a_0 \\ q_1 \\ v_1 \\ a_1 \end{bmatrix}$$

Bu yechim $C^2$-uzluksiz trayektoriyani ta'minlaydi.

---

## 2. ROS2 Hardware Interface Arxitekturasi
ROS2 `ros2_control` tizimi doirasida drayver:
1. `read()`: KRC kontrolleridan real-vaqtda bo'g'in holatini qabul qiladi (`/joint_states`).
2. `write()`: Traektoriya kontrolleri (`JointTrajectoryController`) hisoblagan buyruqlarni KUKA robotiga uzatadi.
