# roxy_lab11.py - SOC Analyst Log Checker
# by Roland

logs = [
    "LOGIN SUCCESS - user: admin",
    "LOGIN FAILED - user: admin",
    "LOGIN FAILED - user: admin",
    "LOGIN FAILED - user: admin",
    "LOGIN FAILED - user: admin",
    "LOGIN SUCCESS - user: roxy",
]

failed = 0

for log in logs:
    print(log)
    if "LOGIN FAILED" in log:
        failed += 1

print("\n--- SOC REPORT ---")
print(f"Total failed logins: {failed}")

if failed >= 3:
    print("ALERT! Possible brute-force attack! Block IP and investigate.")
else:
    print("No threat. Normal activity.")
