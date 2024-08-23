import sys

# 각 줄을 처리
for line in sys.stdin:
    line = line.strip()
    
    # u.data 파일 처리 (탭으로 구분)
    if line.count('\t') == 3:
        user_id, movie_id, rating, timestamp = line.split('\t')
        # 영화 ID와 평점을 출력 (키-값 쌍)
        print(f"{movie_id}\tdata\t{rating}")
    
    # u.item 파일 처리 (파이프로 구분)
    elif line.count('|') >= 2:
        parts = line.split('|')
        movie_id = parts[0]
        movie_name = parts[1]
        # 영화 ID와 영화 이름을 출력 (키-값 쌍)
        print(f"{movie_id}\titem\t{movie_name}")
