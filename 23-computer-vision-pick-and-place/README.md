# 23-Dars: Kompyuter ko'rishi, Hand-Eye kalibratsiyasi va AI Pick-and-Place
## Computer Vision, Hand-Eye Calibration (AX=XB) & AI Pick-and-Place

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-5-advanced-integration-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🎯 1. Maqsad (Goal)
2D/3D mashinaviy ko'rish datchiklari (RGB-D kamera) yordamida robot ishchi organini fazoda nishonga yo'naltirish (Visual Servoing), Tsai-Lenz usulida Hand-Eye ($AX = XB$) kalibratsiyasini hal qilish hamda kamera piksel koordinatalaridan robot bazasi koordinata tizimidagi $\{X, Y, Z, A, B, C\}$ ushlash (Pick-and-Place) traektoriyasini avtomatik hisoblash.

---

### 📊 2. Natija (Result)
1. **Python Vision va Hand-Eye Integratori (`vision_pick_and_place.py`):**
   - Pinhole kamera modeli bo'yicha 2D piksel va chuqurlikdan 3D fazoviy nurni tiklash.
   - Hand-Eye kalibratsiyasi: $T_{base}^{object} = T_{base}^{flange} \cdot T_{flange}^{cam} \cdot T_{cam}^{object}$.
   - KUKA KR 6 flanetsiga moslashtirilgan ushlash koordinatalari kalkulyatori.
2. **Pytest Unit Testlari (`test_vision.py`):**
   - Optik markaz nuri, masshtablash va transformatsiyalar zanjiri to'g'riligi (2/2 test o'tdi).

---

### 🧮 3. Matematik apparat (Mathematics)

$$\mathbf{P}_c = Z_c \cdot K^{-1} [u, v, 1]^T, \quad T_{base}^{object} = T_{base}^{flange} \cdot T_{flange}^{cam} \cdot T_{cam}^{object}$$

Tsai-Lenz formulalari [**docs/derivations.md**](./docs/derivations.md) da keltirilgan.

---

### 💻 4. Ishga tushirish va tekshirish (Execution & Verification)

Python ko'rish modulini sinash:
```bash
uv run --with numpy python src/scripts/vision_pick_and_place.py
```

Konsol chiqishi:
```
=================================================================
Lesson 23: Computer Vision & Hand-Eye Calibration (Pick & Place)
=================================================================

Object in Camera Frame: [66.67, 33.33, 400.00] mm
Grasp Pose in Robot Base Frame:
  X = 516.67 mm
  Y = -66.67 mm
  Z = 950.00 mm
```

Unit testlarni bajarish:
```bash
uv run --with numpy --with pytest pytest src/scripts/test_vision.py
```
Natija: `2 passed in 0.11s`.

---

🔗 **[Bosh Mundarija / Return to Master Syllabus](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
