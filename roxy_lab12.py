# roxy_lab12.py - SOC IP Blocker
# by Roland

logs = [
    "LOGIN FAILED - IP: 192.168.1.10 - user: admin",
    "LOGIN FAILED - IP: 192.168.1.10 - user: admin",
    "LOGIN FAILED - IP: 192.168.1.10 - user: admin",
    "LOGIN FAILED - IP: 192.168.1.10 - user: admin",
    "LOGIN SUCCESS - IP: 192.168.1.20 - user: roxy",
]

blocked_ips = []

for log in logs:
    print(log)
    # Count how many times this IP appears in failed logs
    if "LOGIN FAILED" in log:
        ip = log.split("IP: ")[1].split(" ")[0]
        count = 0
        for l in logs:
            if ip in l and "LOGIN FAILED" in l:
                count += 1
        
        if count >= 3 and ip not in blocked_ips:
            blocked_ips.append(ip)
            print(f">>> BLOCKED IP: {ip} - Too many failed logins!")

print("\n--- SOC REPORT ---")
print(f"Blocked IPs: {blocked_ips}")
if blocked_ips:
    print("Action: IPs blocked and reported to security team.")
else:
    print("No IPs blocked. All clear.")
