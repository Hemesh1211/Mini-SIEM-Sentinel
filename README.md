 # 🛡️ Mini-SIEM Sentinel (Log Analysis & Alerting System)

  ## 🌟 Project Overview
  This project is a **Blue Team** security tool designed to monitor system logs in real-time and detect **Brute Force**
  attacks. It acts as a lightweight SIEM (Security Information and Event Management) system by parsing logs and
  triggering instant alerts.

  ## 🔬 Technical Architecture
  - **Input:** Monitors `/var/log/auth.log` (Linux) or a specified log file.
  - **Detection Engine:** Uses **Regular Expressions (Regex)** to identify "Failed password" patterns.
  - **Intelligence Logic:** Implements a **Sliding Time Window** algorithm. If an IP exceeds 5 failed attempts within
  60 seconds, it is flagged as malicious.
  - **Dispatch:** Integration with **Discord/Telegram Webhooks** for real-time mobile notifications.
  - **Intelligence Logic:** Implements a **Sliding Time Window** algorithm. If an IP exceeds 5 failed attempts within 60 seconds, it is flagged as
  malicious.
  - **Dispatch:** Integration with **Discord/Telegram Webhooks** for real-time mobile notifications.

  ## 🛠️ Setup & Execution
  1. **Install Dependencies:** `pip install requests`
  2. **Configure Webhook:** Open `sentinel.py` and replace `YOUR_DISCORD_OR_TELEGRAM_WEBHOOK_HERE` with your actual webhook URL.
  3. **Run the Sentinel:** `python sentinel.py`

  ## 🎓 Academic Value
  This project demonstrates expertise in:
  - **Log Analysis:** Handling unstructured text data at scale.
  - **Pattern Matching:** Applying Regex for threat detection.
  - **Event Correlation:** Linking multiple events (failed logins) to a single source (IP) over time.
  - **Incident Response:** Automating the notification process to reduce "Mean Time to Detect" (MTTD).