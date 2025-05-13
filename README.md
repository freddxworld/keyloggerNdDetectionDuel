# keyloggerNdDetectionDuel
## Todo
- encrypt key logger
- add code to encrypt logs
- add code to decrypt logs



✅ Keylogger & Detection Duel — Project Roadmap
🟥 Phase 1: Set Up Your Project
## DONE

🟧 Phase 2: Build the Keylogger (Attacker Side)
🔹 Basic Keylogger
Write a Python script that captures keystrokes using pynput

Save captured keystrokes to a local file (keystrokes.log)

🔹 Stealth & Persistence
Hide the log file (prefix with . on Unix, hide attribute on Windows)

Make the keylogger run in the background (use threading)

Set up persistence:

Bash script for Linux (add to .bashrc or systemd)

Registry modification or startup folder for Windows (optional)

🔹 Data Exfiltration (Optional but Fun)
Add feature to email keystrokes every X minutes

Or send keystrokes to a remote server via HTTP POST request

🟨 Phase 3: Build the Detection Script (Defender Side)
🔹 Basic Detection
Write a Python script that lists running processes using psutil

Search for suspicious Python scripts or known process names

Check for files being written in hidden directories or with suspicious names (.log, .txt)

🔹 Behavior Detection
Detect high frequency of keyboard events or file writes

Alert when suspicious activity is detected (print, write to log)

🔹 Advanced Detection (Optional)
Build a Bash script that scans running processes on Linux/Mac

Monitor network traffic for suspicious exfiltration attempts

🟩 Phase 4: Make It SOC-Style (Optional Polishing)
Write a Sigma-style detection rule based on your keylogger

Map the attack and detection to MITRE ATT&CK framework

Store detection logs in SQLite or simple text logs

Bonus: Build a small dashboard using streamlit to show detection alerts

🟦 Phase 5: Documentation & Presentation
Write an attacker playbook: "How this keylogger operates"

Write a defender playbook: "How to detect and respond"

Add a "Lessons Learned" section

Push everything to GitHub (mark attacker code as for demo/educational only)

Bonus: Create a 2-3 minute demo video of your tool in action!

🎯 Optional Stretch Goals (If You’re Feeling Ambitious)
Add screenshot capturing to keylogger

Add support for both Windows and Linux detection

Package the detection tool as a CLI tool with argparse
