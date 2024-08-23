import sys

current_ip = None
current_count = 0
ip = None

for line in sys.stdin:
    line = line.strip()

    ip, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_ip == ip:
        current_count += count
    else:
        if current_ip:
            print(f"{current_ip}\t{current_count}")
        current_count = count
        current_ip = ip

if current_ip == ip:
    print(f"{current_ip}\t{current_count}")
