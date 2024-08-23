import sys

for line in sys.stdin:
    parts = line.split()
    if len(parts) > 0:
        ip_address = parts[0]
        print(f"{ip_address}\t1")