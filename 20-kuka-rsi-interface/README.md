# KUKA RSI (Robot Sensor Interface) Real-Time Architecture
## KUKA RSI (Robot Sensor Interface) real-time interfeysi | Интерфейс реального времени KUKA RSI (Robot Sensor Interface)

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-5-advanced-integration-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🌐 Overview & Multilingual Summary

#### 🇺🇿 O'zbekcha:
KUKA RSI arxitekturasi: tashqi kompyuterdan real vaqtda (<12ms siklda) XML paketlar protokoli orqali to'g'ridan-to'g'ri boshqaruv.

#### 🇷🇺 Русский:
Архитектура KUKA RSI: прямое управление с внешнего ПК в реальном времени (<12 мс) по протоколу XML-пакетов через Ethernet.

#### 🇬🇧 English:
KUKA RSI architecture: direct external real-time control (<12ms deterministic cycle) using XML Ethernet packets.

---

### 🗂️ Directory Structure (Mandatory Boilerplate)
```
20-kuka-rsi-interface/
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
