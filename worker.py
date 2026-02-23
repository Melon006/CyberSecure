import subprocess

def run_scan(socketio, target):

    tools = [
        ("Recon Init", f"ping -c 2 {target}"),
        ("Nmap Scan", f"nmap -F {target}"),
        ("Whois Lookup", f"whois {target}")
    ]

    socketio.emit("update",
    "[SYSTEM] Initializing Cyber Engine...\n")

    for name, cmd in tools:

        socketio.emit("update",
        f"\n[+] {name} Started...\n")

        try:
            result = subprocess.check_output(
                cmd,
                shell=True,
                stderr=subprocess.STDOUT
            ).decode(errors="ignore")

            socketio.emit("update",
            result[:2000])

        except:
            socketio.emit("update",
            "Execution Failed")

    socketio.emit("update",
    "\n[SYSTEM] Scan Completed ✓")
