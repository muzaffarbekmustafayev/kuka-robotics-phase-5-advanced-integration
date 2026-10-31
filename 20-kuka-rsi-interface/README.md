# 20-Dars: KUKA RSI (RobotSensorInterface) va Real-Vaqt UDP integratsiyasi
## KUKA RSI (RobotSensorInterface) Real-Time XML/UDP Socket Integration

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-5-advanced-integration-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🎯 1. Maqsad (Goal)
KUKA RobotSensorInterface (RSI) texnologiyasi asosida tashqi server va KUKA KR C4/C5 boshqaruvchisi o'rtasida $4\text{ ms} / 12\text{ ms}$ real-vaqt rejimida deterministik UDP/IP soket aloqasini o'rnatish, IPOC (Interpolation Cycle Counter) uzluksizligini tahlil qilish hamda real-vaqtda XML formatidagi fazoviy korreksiya signallarini (`RKorr`) generatsiya qilish.

---

### 📊 2. Natija (Result)
1. **Python RSI Real-Time Server Dvigateli (`rsi_socket_server.py`):**
   - KRC dan keluvchi XML paketlarini tezkor parslash (`RIst`, `AIPos`, `IPOC`).
   - IPOC uzluksizligini tekshirish va yo'qolgan paketlar (packet drops) hisobi.
   - Deterministik $4\text{ ms}$ javob paketi generatori (`<Sen Type="ImFree"><RKorr .../>`).
2. **Pytest Unit Testlari (`test_rsi.py`):**
   - XML o'qilishi aniqligi, IPOC xatoliklari hisobi va javob paketi strukturasining 100% to'g'riligi (3/3 test o'tdi).

---

### 🧮 3. Matematik apparat (Mathematics)

$$t_{reply} \le t_{request} + T_{cycle} - \delta_{guard}, \quad \Delta \text{IPOC} = \text{IPOC}_k - \text{IPOC}_{k-1} = 1$$
$$|\Delta p_{xyz}| \le v_{safe} \cdot T_{cycle}$$

RSI xavfsizlik chegaralari va spetsifikatsiyalari [**docs/derivations.md**](./docs/derivations.md) da keltirilgan.

---

### 💻 4. Ishga tushirish va tekshirish (Execution & Verification)

Python RSI dvigatelini sinash:
```bash
uv run --with numpy python src/scripts/rsi_socket_server.py
```

Konsol chiqishi:
```
=================================================================
Lesson 20: KUKA RSI (RobotSensorInterface) Real-Time XML Protocol
=================================================================

Received Robot State:
  IPOC:          10001
  TCP Cartesian: [480.0, 0.0, 435.0, 0.0, 90.0, 0.0]
  Joint Angles:  [0.0, -90.0, 90.0, 0.0, 0.0, 0.0]

Sent XML Reply to KRC:
  <Sen Type="ImFree"><RKorr X="0.0000" Y="0.0000" Z="0.2000" A="0.0000" B="0.0000" C="0.0000"/><IPOC>10001</IPOC></Sen>
```

Unit testlarni bajarish:
```bash
uv run --with numpy --with pytest pytest src/scripts/test_rsi.py
```
Natija: `3 passed in 0.12s`.

---

🔗 **[Bosh Mundarija / Return to Master Syllabus](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
