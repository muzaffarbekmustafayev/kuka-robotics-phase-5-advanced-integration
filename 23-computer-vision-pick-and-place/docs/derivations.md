# Tsai-Lenz Hand-Eye Calibration Theorem (AX = XB) & Modified Rodrigues Vector
## Matematik Isbot va KUKA KR 6 R900-2 uchun Hisoblash

### Asosiy Formula:
$$A_i X = X B_i \quad \text{where } A_i = T_{F_{i+1}}^{F_i}, \quad B_i = T_{C_{i+1}}^{C_i}, \quad X = T_{FLANGE}^{CAMERA}$$

---

### 1. Nazariy Asos va Teorema (Hand-Eye Kalibratsiyasi: $AX = XB$)
Kamerani sanoat roboti flanetsiga o'rnatilganda (Eye-in-Hand), kameraning flanetsga nisbatan aniq 6D fazoviy transformatsiyasini $X = T_{FLANGE}^{CAM}$ aniqlash talab qilinadi.

> **Teorema (Tsai-Lenz Hand-Eye Teoremasi):**
> Robot flanetsi $i$-holatdan $i+1$-holatga harakatlanganda ($A_i$), kamera ham nishonga (ChArUco/shaxmat doskasi) nisbatan mos $B_i$ harakatni amalga oshiradi:
> $$A_i X = X B_i$$
> Matritsaviy ko'rinishda:
> $$\begin{bmatrix} R_A & \vec{t}_A \\ \vec{0}^T & 1 \end{bmatrix} \begin{bmatrix} R_X & \vec{t}_X \\ \vec{0}^T & 1 \end{bmatrix} = \begin{bmatrix} R_X & \vec{t}_X \\ \vec{0}^T & 1 \end{bmatrix} \begin{bmatrix} R_B & \vec{t}_B \\ \vec{0}^T & 1 \end{bmatrix}$$
> Bu ikkita mustaqil tenglamaga ajraladi:
> 1. Aylanish tenglamasi: $R_A R_X = R_X R_B$
> 2. Siljish tenglamasi: $(R_A - I) \vec{t}_X = R_X \vec{t}_B - \vec{t}_A$

### 2. Modifikatsiyalangan Rodrig Vektori Orqali Yechish (Tsai-Lenz Algoritmi)
1. Har bir $A_i$ va $B_i$ burilish matritsalari uchun Rodrigues o'qi $\vec{k}$ va burchagi $\theta$ topiladi.
2. Modifikatsiyalangan Rodrigues vektori yasaladi:
   $$\vec{P} = 2 \tan\left(\frac{\theta}{2}\right) \vec{k}$$
3. Aylanish tenglamasi chiziqli ko'rinishga keladi:
   $$\text{skew}(\vec{P}_A + \vec{P}_B) \cdot \vec{P}_X' = \vec{P}_B - \vec{P}_A$$
4. Eng kichik kvadratlar usuli (SVD / Least Squares) orqali $\vec{P}_X$ topiladi va $R_X$ tiklanadi.
5. $R_X$ ma'lum bo'lgach, siljish $\vec{t}_X$ to'g'ridan-to'g'ri chiziqli tenglamalar tizimidan topiladi:
   $$(R_A - I) \vec{t}_X = R_X \vec{t}_B - \vec{t}_A \quad \blacksquare$$

