import sys

def is_bot(user_agent):
    bot_patterns = ['bot', 'spider', 'crawl', 'AhrefsBot', 'bingbot', 'Googlebot']
    user_agent_lower = user_agent.lower()
    for pattern in bot_patterns:
        if pattern in user_agent_lower:
            return True
    return False

for line in sys.stdin:
    parts = line.strip().split('"')
    
    if len(parts) > 5:
        user_agent = parts[5].strip()  
        if is_bot(user_agent):
            print(f"{user_agent}\t1")  