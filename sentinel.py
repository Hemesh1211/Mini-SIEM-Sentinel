
import re
import time
import requests
from collections import defaultdict

# --- CONFIGURATION ---
LOG_FILE = "dummy_auth.log"
WEBHOOK_URL = "YOUR_WEBHOOK_HERE"
THRESHOLD = 5
TIME_WINDOW = 60

failure_tracker = defaultdict(list)


def send_alert(ip, attempts):
    message = (
        f"🚨 SECURITY ALERT: Brute Force Detected!\n"
        f"IP Address: {ip}\n"
        f"Failed Login Attempts: {attempts}"
    )

    print(f"[!] Dispatching Alert:\n{message}")

    if WEBHOOK_URL == "YOUR_WEBHOOK_HERE":
        print("[!] Webhook URL is not configured. Alert printed locally.")
        return

    try:
        response = requests.post(
            WEBHOOK_URL,
            json={"content": message},
            timeout=10
        )
        response.raise_for_status()
        print("[+] Alert sent successfully.")

    except requests.RequestException as error:
        print(f"[!] Failed to send alert: {error}")


def process_line(line):
    # Match failed SSH password attempts, including IPv4 addresses
    match = re.search(
        r"Failed password for (?:invalid user )?\S+ from "
        r"((?:\d{1,3}\.){3}\d{1,3})\b",
        line
    )

    if not match:
        return

    ip = match.group(1)
    now = time.time()

    # Keep only attempts within the configured time window
    failure_tracker[ip] = [
        timestamp
        for timestamp in failure_tracker[ip]
        if now - timestamp < TIME_WINDOW
    ]

    failure_tracker[ip].append(now)
    attempts = len(failure_tracker[ip])

    print(f"[!] Failed login from {ip}. Count: {attempts}")

    if attempts >= THRESHOLD:
        send_alert(ip, attempts)
        failure_tracker[ip].clear()


def monitor_log():
    print(f"[*] Sentinel Active. Monitoring {LOG_FILE}...")

    try:
        with open(LOG_FILE, "r", encoding="utf-8", errors="replace") as log:
            # Process existing entries first
            for line in log:
                process_line(line)

            print("[+] Initial scan complete. Watching for new entries...")

            # Monitor new entries appended to the log
            while True:
                line = log.readline()

                if not line:
                    time.sleep(1)
                    continue

                process_line(line)

    except FileNotFoundError:
        print(f"[!] Log file not found: {LOG_FILE}")
        print("[!] Create the file or check its path.")

    except KeyboardInterrupt:
        print("\n[*] Sentinel stopped by user.")

    except OSError as error:
        print(f"[!] Error reading log file: {error}")


if __name__ == "__main__":
    monitor_log()
