# ROS 2 Driver Integration & RViz Visualization
## ROS 2 drayverlari integratsiyasi va RViz vizuallashtirish | Интеграция драйверов ROS 2 и визуализация в RViz

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-5-advanced-integration-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🌐 Overview & Multilingual Summary

#### 🇺🇿 O'zbekcha:
ROS 2 (Humble/Iron) arxitekturasi, rasmiy kuka_robot_drivers, robot holatini o'qish va RViz muhitida 3D URDF modelini harakatlantirish.

#### 🇷🇺 Русский:
Архитектура ROS 2 (Humble/Iron), официальные kuka_robot_drivers, чтение состояния и управление 3D URDF в RViz.

#### 🇬🇧 English:
ROS 2 (Humble/Iron) architecture, official kuka_robot_drivers, joint state broadcasting, and RViz URDF visualization.

---

### 🗂️ Directory Structure (Mandatory Boilerplate)
```
21-ros2-driver-integration/
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
