# MoveIt 2 Trajectory Planning & Obstacle Collision Avoidance
## MoveIt 2 yordamida to'siqlarni aylanib o'tuvchi harakat rejalashtirish | Планирование траекторий с обходом препятствий в MoveIt 2

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-5-advanced-integration-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🌐 Overview & Multilingual Summary

#### 🇺🇿 O'zbekcha:
MoveIt 2 kutubxonasi, OMPL rejalashtiruvchilari, dinamik paydo bo'lgan to'siqlarni chetlab o'tish (Collision Avoidance).

#### 🇷🇺 Русский:
Библиотека MoveIt 2, алгоритмы OMPL, динамический обход препятствий в рабочей зоне манипулятора.

#### 🇬🇧 English:
MoveIt 2 framework, OMPL motion planners, dynamic collision manifold detection, and obstacle avoidance execution.

---

### 🗂️ Directory Structure (Mandatory Boilerplate)
```
22-moveit2-trajectory-planning/
├── src/
│   ├── krl/            # Production KRL code (.src, .dat) [All code & comments in English]
│   └── scripts/        # Python verification scripts (.py) [All code & comments in English]
├── sim/                # KUKA.Sim Pro layouts (.vcmx), URDF and CAD models
├── docs/               # Theoretical diagrams, figures, and proofs
├── CLAUDE.md           # AI developer instructions
└── README.md           # Trilingual guide (Uzbek, Russian, English)
```

---

### 🧮 Mathematical Foundations & Verification
All formulas, derivations, and theorems for this lesson are detailed in [**docs/derivations.md**](./docs/derivations.md).
Runnable Python verification scripts are provided in `src/scripts/verify_theorem.py`.

To run the verification test:
```bash
uv run --with numpy python src/scripts/verify_theorem.py
```

---
🔗 **[Return to Master Syllabus / Bosh Mundarija](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
