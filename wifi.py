import os
import re
import subprocess
import time

def check_airmon():
    result = subprocess.run(["which", "airmon-ng"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("Error: airmon-ng is not installed. Please install it using: sudo apt install aircrack-ng")
        exit()

def list_interfaces():
    result = subprocess.run(["iwconfig"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    interfaces = re.findall(r"^\w+", result.stdout, re.MULTILINE)
    print("Available Network Interfaces:")
    for interface in interfaces:
        print(f"- {interface}")
    return interfaces

def start_monitor_mode(interface):
    print(f"Starting monitor mode on {interface}...")
    subprocess.run(["sudo", "airmon-ng", "start", interface])

def stop_monitor_mode(interface):
    print(f"Stopping monitor mode on {interface}...")
    subprocess.run(["sudo", "airmon-ng", "stop", interface])

def scan_wifi(interface):
    print(f"Scanning for Wi-Fi networks on {interface}...")
    scan_result_file = "/tmp/wifi_scan_results"
    try:
        with open(scan_result_file, "w") as f:
            process = subprocess.Popen(["sudo", "airodump-ng", interface], stdout=f, stderr=subprocess.PIPE)
            time.sleep(10)  # Scan for 10 seconds
            process.terminate()

        with open(scan_result_file, "r") as f:
            data = f.readlines()
        
        networks = []
        for line in data:
            match = re.search(r"([\dA-F]{2}(:|-)){5}[\dA-F]{2}", line, re.IGNORECASE)
            if match:
                networks.append(line.strip())
        
        print("\n--- Wi-Fi Networks Found ---")
        for network in networks:
            print(network)

    except KeyboardInterrupt:
        print("\nScanning interrupted.")
    finally:
        if os.path.exists(scan_result_file):
            os.remove(scan_result_file)

if __name__ == "__main__":
    check_airmon()
    interfaces = list_interfaces()
    if not interfaces:
        print("No network interfaces found!")
        exit()
    
    selected_interface = interfaces[0]
    
    try:
        start_monitor_mode(selected_interface)
        scan_wifi(f"{selected_interface}mon")
    finally:
        stop_monitor_mode(selected_interface)
