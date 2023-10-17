# HW3-BLE-Central-Programming

Group : 9  
Member : B09901043 陳昱樺 B09901134 林容丞

Function
---
Here are what this project does:
1. Raspberry Pi runs a Python program that can communicate with BLE Tool in an Android  phone.
2. Read the CCCD value, and print it in the console.
3. Change the CCCD value to 0x0002.
4. Read the CCCD value again, and print it in the console.

Prerequisites
---
There are three things a user should prepare to run this project:
* Android phone with app BLE Tool
* Raspberry Pi 3
* Python

Usage
---
Here are some steps to run this project properly:
1. Download Raspberry Pi OS Lite (32-bit) image. 
2. Flash the image to a micro SD card. 
3. Add this line at the end of /boot/config.txt: 
```
enable_uart = 1
```
4. Connect USB-TTL serial console to Raspberry Pi using minicom in Linux host. 
5. Check if the path is correct for Serial Device using command: 
```
sudo minicom -s
```
6. Run minicom using command: 
```
sudo minicom
```
7. Set up wifi configuration using raspi-config (System Options → Wireless LAN → set country / SSID / password). 
8. Run command
```
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```
and add this to the bottom of the file: 
```
network={
    ssid="yourSSID"
    psk="yourPassword"
}
```
9. Install python3-pip / libglib2.0-dev / bluepy. 
10. Select Gatt Server in BLE Tool on the Android phone. 
11. Start advertising the service on BLE Tool. 
12. Run ble_scan_connect.py on RPi. 
13. Halt RPi before cutting the power off by command: 
```
sudo halt
```

License
---
None.

Acknowledgements
---
Here are some resources we refer to to finish this project:
* Course slides: Develop Environment for Embedded Systems, BLE Introduction and Labs using Raspberry Pi
