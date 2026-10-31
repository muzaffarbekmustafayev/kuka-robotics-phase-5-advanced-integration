# Konfiguratsion Fazoda Harakat Rejalashtirish (C-Space RRT) va To'qnashuvdan Qochish

## 1. Konfiguratsion Faza ($\mathcal{C}$-Space) Dekompozitsiyasi
Robot bo'g'inlari burchaklari fazosi $\mathcal{C} = \prod_{i=1}^6 [q_{min, i}, q_{max, i}] \subset \mathbb{R}^6$ ikkita tutash bo'lmagan to'plamga bo'linadi:

$$\mathcal{C} = \mathcal{C}_{free} \cup \mathcal{C}_{obs}, \quad \mathcal{C}_{free} \cap \mathcal{C}_{obs} = \emptyset$$

bu yerda $\mathcal{C}_{obs}$ — robotning o'z-o'ziga yoki tashqi to'siqlarga to'qnashuvchi bo'g'in burchaklari to'plami.

---

## 2. RRT (Rapidly-exploring Random Tree) Algoritmi
Har bir iteratsiyada tasodifiy konfiguratsiya generatsiya qilinadi (maqsad tomon siljish ehtimoli $p_{bias}$ bilan):

$$\mathbf{q}_{rand} = \begin{cases} \mathbf{q}_{goal}, & \text{agar } \xi < p_{bias} \\ \mathcal{U}(\mathcal{C}), & \text{aksincha} \end{cases}$$

Eng yaqin tugun $\mathbf{q}_{near} \in \mathcal{T}$:
$$\mathbf{q}_{near} = \arg\min_{\mathbf{q} \in \mathcal{T}} \|\mathbf{q} - \mathbf{q}_{rand}\|$$

Qadam siljishi ($\epsilon$-step):
$$\mathbf{q}_{new} = \mathbf{q}_{near} + \epsilon \cdot \frac{\mathbf{q}_{rand} - \mathbf{q}_{near}}{\|\mathbf{q}_{rand} - \mathbf{q}_{near}\|}$$

Agar $[\mathbf{q}_{near}, \mathbf{q}_{new}]$ segmenti to'qnashuvsiz ($\subset \mathcal{C}_{free}$) bo'lsa, $\mathbf{q}_{new}$ daraxtga qo'shiladi.

---

## 3. Trayektoriyani Silliqlash (Shortcut Smoothing)
Dastlabki topilgan RRT yo'li tasodifiy silkinishlarga ega bo'ladi. Shortcut algoritmi ixtiyoriy ikki uzoq nuqta $\mathbf{q}_i$ va $\mathbf{q}_j$ ($j > i + 1$) orasini to'g'ri chiziq bilan bog'laydi:

$$\forall \alpha \in [0, 1]: (1 - \alpha) \mathbf{q}_i + \alpha \mathbf{q}_j \in \mathcal{C}_{free}$$
Agar shart bajarilsa, oraliqdagi barcha keraksiz nuqtalar o'chirilib, yo'l uzunligi va harakat vaqti minimallashtiriladi. $\blacksquare$
