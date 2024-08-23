import sys

bot_count = 0

for line in sys.stdin:
    _, count = line.strip().split('\t')
    bot_count += int(count)

print(f"Total Bot Requests: {bot_count}")
