# 22-Dars: MoveIt2, Konfiguratsion Faza (C-Space) va RRT Rejalashtiruvchisi
## MoveIt2 Trajectory Planning, C-Space & RRT Obstacle Avoidance

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-5-advanced-integration-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🎯 1. Maqsad (Goal)
Murakkab to'siqli sanoat muhitida KUKA KR 6 roboti uchun MoveIt2 / OMPL tamoyillari asosida 6-DOF konfiguratsion fazoda ($\mathcal{C} = \mathbb{R}^6$) to'qnashuvsiz optimal yo'lni rejalashtirish: RRT (Rapidly-exploring Random Tree) algoritmi, to'siqlarni tekshirish (Collision Checking) va trayektoriyani optimallashtiruvchi Shortcut Smoothing vositasini ishlab chiqish.

---

### 📊 2. Natija (Result)
1. **Python C-Space RRT Rejalashtiruvchisi (`cspace_rrt_planner.py`):**
   - 6 o'qli bo'g'inlar fazosida ehtimolli tasodifiy daraxt (RRT) kengayishi.
   - Maqsadga tortishish koeffitsienti (Goal-biasing).
   - Fazoviy to'qnashuvlarni tekshirish (Collision Detector).
   - Trayektoriyani optimallashtirish va oraliq tugunlarni qisqartirish (Shortcut Smoothing).
2. **Pytest Unit Testlari (`test_rrt.py`):**
   - Erkin fazoda to'g'ri rejalash va to'siqni aylanib o'tish tekshiruvlari (2/2 test o'tdi).

---

### 🧮 3. Matematik apparat (Mathematics)

$$\mathbf{q}_{new} = \mathbf{q}_{near} + \epsilon \frac{\mathbf{q}_{rand} - \mathbf{q}_{near}}{\|\mathbf{q}_{rand} - \mathbf{q}_{near}\|}, \quad [\mathbf{q}_{near}, \mathbf{q}_{new}] \subset \mathcal{C}_{free}$$

Teoremalar va to'liq tahlil [**docs/derivations.md**](./docs/derivations.md) da berilgan.

---

### 💻 4. Ishga tushirish va tekshirish (Execution & Verification)

Python rejalashtiruvchisini sinash:
```bash
uv run --with numpy python src/scripts/cspace_rrt_planner.py
```

Konsol chiqishi:
```
=================================================================
Lesson 22: C-Space RRT Trajectory Planner & Obstacle Avoidance
=================================================================

Path Successfully Planned! Number of Waypoints: 8
  Start: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0] rad
  Goal:  [0.5, 1.2, 0.8, 0.0, 0.0, 0.0] rad
```

Unit testlarni bajarish:
```bash
uv run --with numpy --with pytest pytest src/scripts/test_rrt.py
```
Natija: `2 passed in 0.13s`.

---

🔗 **[Bosh Mundarija / Return to Master Syllabus](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
