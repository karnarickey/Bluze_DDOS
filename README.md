# 💥 Bluetooth DoS GUI Tool - Powered by BlueZ + Python

A tactical GUI-based Bluetooth Denial-of-Service tool built for ethical hackers, by an ethical hacker (Saksham Karn).

This project leverages the power of `l2ping` flood attacks and Python's multithreading to test the resilience of Bluetooth devices like Earpods, speakers, headsets, and more. All wrapped inside a clean, simple GUI interface.

---

## ⚙️ Features

✅ **Real-time Bluetooth Scanning** (Manual + Auto Refresh)  
🧠 **Select Target from Dropdown List**  
📦 **Custom Packet Size & Thread Count**  
💥 **Launch DoS Attack with One Click**  
📡 **Live Thread Execution Monitor (per thread logs)**  
🛡️ **Educational & Ethical Use Only**

---

## 🖼️ Screenshots
<img width="1920" height="1080" alt="Screenshot (258)" src="https://github.com/user-attachments/assets/b8612010-932d-4dc5-b9b8-401955bed9d5" />


## 🧰 Requirements

- Python 3.x  
- Linux OS (Ubuntu, Kali, Parrot OS)  
- Bluetooth adapter (internal or USB)  
- BlueZ stack (`l2ping`, `hcitool`)

### 📦 Install dependencies:
```bash
sudo apt update
gitclone https://github.com/karnarickey/Bluze_DDOS.git
cd Bluze_DDOS
sudo apt install bluez l2ping python3-tk
python3 bluetooth.py
