# KUKA RSI (RobotSensorInterface) Real-Time Protokoli

## 1. RSI Arxitekturasi va Deterministik Sikl
KUKA RSI (RobotSensorInterface) tashqi kompyuter (Linux RT-Preempt, ROS2 yoki Python server) bilan robot kontrolleri (KRC) o'rtasida UDP protokoli orqali qat'iy $4\text{ ms}$ yoki $12\text{ ms}$ chastotada bog'lanishni ta'minlaydi:

$$T_{cycle} \in \{0.004\text{ s}, 0.012\text{ s}\} \quad (250\text{ Hz} \dots 83.3\text{ Hz})$$

### Jitter va Vaqt Cheklovi (Watchdog Deadline):
Robot har bir siklda o'zining joriy holatini XML shaklida jo'natadi va javob paketini kutadi:
$$t_{reply} \le t_{request} + T_{cycle} - \delta_{guard}$$
Agar javob belgilangan vaqt ichida yetib kelmasa yoki IPOC (Interpolation Cycle Counter) uzilsa:
$$\text{IPOC}_{k} \neq \text{IPOC}_{k-1} + 1$$
KRC kontrolleri darhol xavfsizlik to'xtashini (RSI Stop) faollashtiradi.

---

## 2. XML Protokoli Strukturasi
**KRC dan keluvchi telemetriya paketi:**
```xml
<Rob Type="KUKA">
  <RIst X="480.0" Y="0.0" Z="435.0" A="0.0" B="90.0" C="0.0"/>
  <AIPos A1="0.0" A2="-90.0" A3="90.0" A4="0.0" A5="0.0" A6="0.0"/>
  <IPOC>10001</IPOC>
</Rob>
```

**Tashqi serverdan yuboriladigan real-time tuzatish (Correction):**
```xml
<Sen Type="ImFree">
  <RKorr X="0.0" Y="0.0" Z="0.2" A="0.0" B="0.0" C="0.0"/>
  <IPOC>10001</IPOC>
</Sen>
```
bu yerda `RKorr` — joriy $4\text{ ms}$ siklda flanetsga beriladigan relyativ siljish ($\Delta X, \Delta Y, \Delta Z$).
Maksimal ruxsat etilgan bir siklli siljish chegaralangan:
$$|\Delta p_{xyz}| \le v_{max} \cdot T_{cycle} = 250 \text{ mm/s} \times 0.004\text{ s} = 1.0\text{ mm}$$
Bu chegaradan oshish kinetik silkinish (jerk) va kontroller xatosiga sabab bo'ladi.
