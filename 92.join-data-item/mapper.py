import sys

# 각 줄을 처리
for line in sys.stdin:
    line = line.strip()
    
    # u.data 파일 처리
    if line.count('\t') == 3:
        user_id, movie_id, rating, timestamp = line.split('\t')
        print(f"{movie_id}\tdata\t{user_id}\t{rating}")
    
    # u.item 파일 처리
    elif line.count('|') >= 2:
        parts = line.split('|')
        movie_id = parts[0]
        movie_title = parts[1]
        print(f"{movie_id}\titem\t{movie_title}")
