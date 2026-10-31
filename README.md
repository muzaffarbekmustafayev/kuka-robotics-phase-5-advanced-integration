# Phase 5: External Interfaces, ROS2 & Robotics AI
## 5-Bob: Tashqi Interfeyslar, ROS2 va Sun'iy Intellekt
### Глава 5: Внешние Интерфейсы, ROS2 и Искусственный Интеллект

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Topics](https://img.shields.io/badge/Topics-kuka--robotics--course%20%7C%20mechatronics%20%7C%20krl--programming%20%7C%20ros2--robotics%20%7C%20samdu%20%7C%20tsu-blue.svg)](#)

---

### 🌐 Phase Description (Trilingual)

#### 🇺🇿 O'zbekcha:
KUKA RSI real vaqtli interfeysi, ROS2 drayverlari, MoveIt2 to'siqlarni aylanib o'tish va Computer Vision integratsiyasi.

#### 🇷🇺 Русский:
Интерфейс реального времени KUKA RSI, драйверы ROS2, планирование траекторий в MoveIt2 и компьютерное зрение.

#### 🇬🇧 English:
KUKA RSI real-time interface, official ROS 2 drivers, MoveIt 2 obstacle avoidance, and Computer Vision integration.

---

### 📑 Lessons Curriculum / Darslar Mundarijasi / Содержание уроков

* [**20-kuka-rsi-interface**: KUKA RSI (Robot Sensor Interface) Real-Time Architecture](./20-kuka-rsi-interface)
  * 🇺🇿 KUKA RSI arxitekturasi: tashqi kompyuterdan real vaqtda (<12ms siklda) XML paketlar protokoli orqali to'g'ridan-to'g'ri boshqaruv.
  * 🇷🇺 Архитектура KUKA RSI: прямое управление с внешнего ПК в реальном времени (<12 мс) по протоколу XML-пакетов через Ethernet.
  * 🇬🇧 KUKA RSI architecture: direct external real-time control (<12ms deterministic cycle) using XML Ethernet packets.

* [**21-ros2-driver-integration**: ROS 2 Driver Integration & RViz Visualization](./21-ros2-driver-integration)
  * 🇺🇿 ROS 2 (Humble/Iron) arxitekturasi, rasmiy kuka_robot_drivers, robot holatini o'qish va RViz muhitida 3D URDF modelini harakatlantirish.
  * 🇷🇺 Архитектура ROS 2 (Humble/Iron), официальные kuka_robot_drivers, чтение состояния и управление 3D URDF в RViz.
  * 🇬🇧 ROS 2 (Humble/Iron) architecture, official kuka_robot_drivers, joint state broadcasting, and RViz URDF visualization.

* [**22-moveit2-trajectory-planning**: MoveIt 2 Trajectory Planning & Obstacle Collision Avoidance](./22-moveit2-trajectory-planning)
  * 🇺🇿 MoveIt 2 kutubxonasi, OMPL rejalashtiruvchilari, dinamik paydo bo'lgan to'siqlarni chetlab o'tish (Collision Avoidance).
  * 🇷🇺 Библиотека MoveIt 2, алгоритмы OMPL, динамический обход препятствий в рабочей зоне манипулятора.
  * 🇬🇧 MoveIt 2 framework, OMPL motion planners, dynamic collision manifold detection, and obstacle avoidance execution.

* [**23-computer-vision-pick-and-place**: Computer Vision, Hand-Eye Calibration & Visual Pick-and-Place](./23-computer-vision-pick-and-place)
  * 🇺🇿 Pinhole kamera modeli, OpenCV cv2.solvePnP, cv2.Rodrigues, Hand-Eye AX=XB (Tsai-Lenz) kalibratsiyasi va robotlashtirilgan saralash.
  * 🇷🇺 Модель Pinhole-камеры, cv2.solvePnP, cv2.Rodrigues, калибровка Hand-Eye AX=XB (метод Цая-Ленца) и сортировка деталей.
  * 🇬🇧 Pinhole camera model, cv2.solvePnP, cv2.Rodrigues, Hand-Eye calibration AX=XB (Tsai-Lenz method), and visual pick-and-place.

---

### 🏛️ Repository Internal Structure
```
kuka-robotics-phase-5-advanced-integration/
├── 20-kuka-rsi-interface/
├── 21-ros2-driver-integration/
├── 22-moveit2-trajectory-planning/
├── 23-computer-vision-pick-and-place/
```

---

### 👥 Academic Alliance & Authorship
* **Author / Muallif:** Muzaffarbek Mustafayev
* **Academic Partners:** Samarkand State University (SamDU) & Tomsk State University (TSU)
* 🔗 **[Master Syllabus Navigator](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
