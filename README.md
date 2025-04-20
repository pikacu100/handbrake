# 🕹️ Handbrake – Arduino-based USB Controller

This project allows you to build a DIY USB handbrake controller using an Arduino, a potentiometer, and a bit of Python magic. Data is sent via serial communication from the Arduino to your PC, where Python reads the input and uses **vJoy** to simulate a joystick axis — perfect for sim racing games like Assetto Corsa, Dirt Rally, or BeamNG.

---

## 🔩 How It Works

1. **Arduino** reads analog values from a **potentiometer** (connected to a handbrake lever).
2. It sends the values over **Serial communication** to the **PC**.
3. A **Python script** running on the PC reads the data.
4. The script uses **pyvjoy** to pass the value to a virtual joystick created by **vJoy**.

---

## 🧰 Components

- Arduino UNO / Nano / Micro
- Potentiometer (e.g., 10k linear)
- USB cable
- PC with:
- Python 3
- vJoy installed
- pyserial & pyvjoy Python packages
