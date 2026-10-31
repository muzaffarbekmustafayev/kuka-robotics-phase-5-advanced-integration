# Kompyuter Ko'rishi, Hand-Eye Kalibratsiyasi va Grasping Geometriyasi

## 1. Pinhole Kamera Proyeksiyasi va Orqaga Qaytarish (Back-projection)
Kamera koordinatalaridagi 3D nuqta $\mathbf{P}_c = [X_c, Y_c, Z_c]^T$ ning $2D$ tasvir piksel tekisligidagi proyeksiyasi:

$$s \begin{bmatrix} u \\ v \\ 1 \end{bmatrix} = K \begin{bmatrix} X_c \\ Y_c \\ Z_c \end{bmatrix} = \begin{bmatrix} f_x & 0 & c_x \\ 0 & f_y & c_y \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} X_c \\ Y_c \\ Z_c \end{bmatrix}$$

bu yerda $s = Z_c$ (chuqurlik / depth).
Orqaga qaytarish (Piksel + Chuqurlik $\to$ 3D nuqta):
$$\mathbf{P}_c = Z_c \cdot K^{-1} \begin{bmatrix} u \\ v \\ 1 \end{bmatrix} = \begin{bmatrix} (u - c_x) \frac{Z_c}{f_x} \\ (v - c_y) \frac{Z_c}{f_y} \\ Z_c \end{bmatrix}$$

---

## 2. Hand-Eye Kalibratsiyasi ($AX = XB$ Tenglamasi)
Robot flanetsiga o'rnatilgan kamera (Eye-in-Hand) uchun:
$$A_i = T_{flange, i+1}^{-1} \cdot T_{flange, i}$$
$$B_i = T_{cam\_target, i+1} \cdot T_{cam\_target, i}^{-1}$$
$$A_i X = X B_i$$
bu yerda $X = T_{flange}^{cam}$ — aniqlanishi lozim bo'lgan doimiy montaj transformatsiyasi.

Tsai-Lenz metodiga ko'ra o'q-burchak $(\mathbf{k}, \theta)$ representatsiyasi orqali burilish qismi:
$$\text{skew}(\mathbf{k}_{A} + \mathbf{k}_{B}) \mathbf{P}_X = 2 (\mathbf{k}_{A} - \mathbf{k}_{B})$$
tenglamalar sistemasini eng kichik kvadratlar usuli (Least Squares) bilan yechiladi.

---

## 3. Robot Bazasi Bo'yicha Yakuniy Grasp Pozitsiyasi
Aniqlangan obyektni robot manipulyatori tomonidan ushlash (Pick-and-Place) uchun transformatsiyalar zanjiri:

$$T_{base}^{object} = T_{base}^{flange} \cdot T_{flange}^{cam} \cdot T_{cam}^{object}$$

Bu transformatsiya natijasida olingan pozitsiya va yo'nalish to'g'ridan-to'g'ri KRL formatidagi `{X, Y, Z, A, B, C}` nishoniga aylanadi. $\blacksquare$
