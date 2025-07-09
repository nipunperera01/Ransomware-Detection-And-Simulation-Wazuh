# 🛡️ Ransomware Simulation & Detection using Wazuh SIEM

This project demonstrates a realistic ransomware attack simulation using Kali Linux and Ubuntu Server, with detection and monitoring handled by the Wazuh SIEM platform.

---

## 🎯 Objective

- Simulate a ransomware-style attack from a Kali Linux attacker machine.
- Detect malicious file activity using Wazuh's File Integrity Monitoring (FIM) on a Ubuntu server.
- Learn how SIEM tools identify suspicious file behavior like encryption and deletion.

---

## 🧪 Lab Environment

| Component       | Description                                  |
|----------------|----------------------------------------------|
| 🧑‍💻 Attacker    | Kali Linux (deployed ransomware script)   |
| 🛡️ Defender     | Ubuntu Server with Wazuh agent               |
| 🎯 Target       | File system on Ubuntu (`~/ransomware_test`)   |
| 📊 SIEM         | Wazuh    |

---

## 🧰 Tools Used

- Kali Linux (Attacker)
- Ubuntu Server 22.04 (Target)
- Wazuh OVA 4.12.0 (SIEM Platform)
- Python (Simulated Ransomware Script)

---

## 🐍 Ransomware Simulation Script

### Deployed from Kali via SSH to the Ubuntu server 

-(`~fake_ransomware.py`)

## 📂 This script:

- Encodes original files with base64
- Creates .enc encrypted files
- Deletes the originals

---

## 🛡️ Detection via Wazuh

- Wazuh Agent on the Ubuntu machine detected:
- File deletions (original .`~.txt`, `~.doc`, `~.csv`)
- New encrypted files (`~.enc`)
- Alerts logged in real time via Wazuh Dashboard

---

## 🔍 Sample Alert Types

- Alert Type	Description
- deleted	Original file removed
- added	.enc file created (fake encryption)
- modified	Optional if file was edited

---

## 📸 Screenshots

- fake_ransomware py creation.png
- sftp by kali linux(attasker).png
- ssh and execute ransomeware script.png
- SIEM notifications by FIM.png
- activity summary in wazuh.png
- detection-deleted files by the attacker.png
- detection-modified files by attacker.png
- detection-newly added files by attacker.png
- check.png

---

## 🧠 What I Learned

- How to simulate ransomware behavior safely
- Role of File Integrity Monitoring in detection
- Importance of logs and SIEM in incident response
- Basic offensive + defensive coordination

---

## 🚀 Next Phase

- ♻️ Simulate file recovery from backups
- 🔐 Harden system with Fail2Ban or SFTP restrictions

---

## 👤 Author
Nipun Perera
Network Security Undergraduate – Sri Lanka
