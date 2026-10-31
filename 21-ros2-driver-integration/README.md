# 21-Dars: ROS2 drayver integratsiyasi va ros2_control arxitekturasi
## ROS2 Driver Integration, Hardware Interface & ros2_control

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-5-advanced-integration-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🎯 1. Maqsad (Goal)
ROS2 (Robot Operating System 2) muhitida KUKA KR 6 manipulyatori uchun `ros2_control` hardware interface modulini yaratish, `sensor_msgs/msg/JointState` telemetriyasini boshqarish hamda boshlang'ich va yakuniy tezlanishlari nolga teng bo'lgan ($C^2$ silliqlikdagi) 5-darajali kvintik ko'phad splayn trayektoriyasini hisoblash.

---

### 📊 2. Natija (Result)
1. **Python ROS2 Hardware Ko'prigi (`kuka_ros2_interface.py`):**
   - 6 o'q bo'yicha `JointState` xabarlarini ishlab chiqarish.
   - Analitik 5-darajali kvintik ko'phad ($s(t) = \sum_{i=0}^5 a_i t^i$) generatori (boshlang'ich va chekka nuqtalarda tezlik va tezlanish nolga teng).
   - Real-vaqt tezlik va pozitsiya yangilanish mexanizmi.
2. **Pytest Unit Testlari (`test_ros2.py`):**
   - Kvintik chegaraviy shartlar ($v_0=v_1=0, a_0=a_1=0$) va holat massivlari aniqligi (2/2 test o'tdi).

---

### 🧮 3. Matematik apparat (Mathematics)

$$s(t) = a_0 + a_1 t + a_2 t^2 + a_3 t^3 + a_4 t^4 + a_5 t^5$$
$$\dot{s}(0)=\dot{s}(T)=0, \quad \ddot{s}(0)=\ddot{s}(T)=0$$

To'liq matritsaviy yechim [**docs/derivations.md**](./docs/derivations.md) da keltirilgan.

---

### 💻 4. Ishga tushirish va tekshirish (Execution & Verification)

Python interfeysini sinash:
```bash
uv run --with numpy python src/scripts/kuka_ros2_interface.py
```

Konsol chiqishi:
```
=================================================================
Lesson 21: ROS2 Hardware Interface & Quintic Trajectory Solver
=================================================================

Interpolated Quintic Trajectory for Joint 1:
  Duration: 2.00 s
  Initial Pos: 0.0000 rad, Final Pos: 1.5708 rad
  Peak Vel:    1.4726 rad/s
  Start/End Velocity: 0.0000 / 0.0000 rad/s (Smooth Jerk-Free)
```

Unit testlarni bajarish:
```bash
uv run --with numpy --with pytest pytest src/scripts/test_ros2.py
```
Natija: `2 passed in 0.12s`.

---

🔗 **[Bosh Mundarija / Return to Master Syllabus](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
