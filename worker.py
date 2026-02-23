import subprocess
from urllib.parse import urlparse

def clean_target(target):

    if "http" in target:
        target = urlparse(target).netloc

    return target.replace("www.","")


def run_scan(socketio,target):

    target = clean_target(target)

    socketio.emit(
        "update",
        f"[SYSTEM] Target Locked → {target}\n"
    )

    tools=[
        ("Ping",f"ping -c 2 {target}"),
        ("Nmap Fast Scan",f"nmap -F {target}"),
        ("Whois",f"whois {target}")
    ]

    for name,cmd in tools:

        socketio.emit(
        "update",
        f"\n[+] Running {name}...\n")

        try:
            result=subprocess.check_output(
                cmd,
                shell=True,
                stderr=subprocess.STDOUT
            ).decode(errors="ignore")

            socketio.emit(
                "update",
                result[:1500])

        except Exception as e:
            socketio.emit(
                "update",
                f"Scan Failed: {name}\n")

    socketio.emit(
        "update",
        "\n✓ Recon Completed"
    )
