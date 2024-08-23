import sys

last_hour = None
total_count = 0

for line in sys.stdin:
    hour, count = line.strip().split('\t')
    count = int(count)

    if last_hour == hour:
        total_count += count
    else:
        if last_hour is not None:
            print(f'{last_hour}\t{total_count}')
        last_hour = hour
        total_count = count

if last_hour == hour:
    print(f'{last_hour}\t{total_count}')