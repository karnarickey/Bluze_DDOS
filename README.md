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

- Python3
- Linux OS (Ubuntu, Kali, Parrot OS)  
- Bluetooth adapter (internal or USB)  
- BlueZ stack (`l2ping`, `hcitool`)

### 📦 Install dependencies:
```bash
sudo apt update
git clone https://github.com/karnarickey/Bluze_DDOS.git
cd Bluze_DDOS
sudo apt install bluez l2ping python3-tk
python3 bluetooth.py
```
## 🚀How It Works
Launch the tool (GUI auto-opens)
Scan or auto-scan for Bluetooth devices
Select target device (MAC + Name)
Set packet size & thread count
Press "Start Attack" and monitor live logs

## ⚠️Legal Notice
This tool is intended strictly for educational, ethical, and authorized penetration testing only.
Unauthorized use on other people's devices is illegal.
You are solely responsible for how you use this tool.

## 💡Project By
👨‍💻Saksham karn
Ethical Hacker | Security Learner | Creator of Chaos for a Cause
## 📅 Created: July 2025

## 💭 Future Upgrades
Attack timer with countdown
Save logs to file
Kill switch for attack threads
Bluetooth MAC sniffer (Windows edition)
Dark mode GUI

## 📩 Want to Contribute?
Pull requests are welcome! Just keep it legal, lean, and clean.
Open an issue if you’ve got ideas, bugs, or want to collab.

## 🙏 Thanks for Scanning By
If you learned something or smiled at the power of GUI-based Bluetooth madness, give this repo a ⭐
Stay sharp. Stay ethical. Hack with purpose. 🧠💻


