import subprocess
import re

def get_bssid_windows():
    # Run the netsh command
    result = subprocess.run(
        ["netsh", "wlan", "show", "interfaces"],
        capture_output=True,
        text=True
    )

    # Search for BSSID line
    match = re.search(r"BSSID\s*:\s*([0-9A-Fa-f:]{17})", result.stdout)
    if match:
        return str(match.group(1)).upper()
    else:
        return None
