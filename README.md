# created by <----SAKSHAM KARN---->
# Bluze_DDOS
A GUI-based Bluetooth DoS tool built with Python and BlueZ. It scans nearby devices and launches multithreaded l2ping flood attacks with real-time status logging. Designed for ethical hacking, penetration testing, and Bluetooth security research on Linux.
# 🔥 Bluetooth DoS Attack Tool (BlueZ-Based) - GUI Edition

A Python-based GUI tool that performs Bluetooth Denial-of-Service (DoS) attacks using `l2ping` flood packets. Designed for **educational and authorized testing purposes**, this utility helps security researchers assess the robustness of Bluetooth-enabled devices against packet flood attacks.

---

## 🧰 Features

- ✅ **Tkinter GUI Interface** – Clean, easy-to-use interface for launching attacks.
- 🔍 **Manual & Auto Bluetooth Scanning** – Continuously scan nearby Bluetooth devices every 5 seconds.
- 🎯 **Target Selection** – Choose target device via dropdown (MAC + Name).
- 📦 **Custom Packet Size Input** – Set payload size for each L2CAP echo request.
- 🧵 **Multi-threaded Attack Launcher** – Launch multiple attack threads simultaneously.
- 📡 **Real-Time Thread Status Monitoring** – Get live logs of thread activity (start, success, timeout, error).
- ⚙️ **Cross-Platform GUI (Linux only)** – Windows not supported due to `l2ping` dependency.

---

## ⚙️ Requirements

- Python 3.x  
- Linux OS (Ubuntu, Kali, Parrot, etc.)  
- Bluetooth Adapter (internal or USB)  
- BlueZ Stack with `l2ping` installed

### 🔧 Install Dependencies:
```bash
sudo apt update
gitclone https://github.com/karnarickey/Bluze_DDOS.git
cd Bluze_DDOS
sudo apt install bluez l2ping python3-tk
python3 bluetooth.py

