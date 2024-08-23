import sys

current_movie_id = None
movie_title = None
ratings = []

# 각 키에 대해 처리
for line in sys.stdin:
    line = line.strip()
    parts = line.split('\t')
    
    if len(parts) == 4:
        movie_id, source, user_id, rating = parts
    elif len(parts) == 3:
        movie_id, source, movie_title = parts
    else:
        continue

    if current_movie_id == movie_id:
        if source == "item":
            movie_title = movie_title
        elif source == "data":
            ratings.append((user_id, rating))
    else:
        # 이전 영화에 대한 결과 출력
        if current_movie_id and movie_title:
            for user_id, rating in ratings:
                print(f"{user_id}\t{movie_title}\t{rating}")
        
        # 새로운 영화로 업데이트
        current_movie_id = movie_id
        ratings = []
        if source == "item":
            movie_title = movie_title
        elif source == "data":
            ratings.append((user_id, rating))

# 마지막 영화 처리
if current_movie_id and movie_title:
    for user_id, rating in ratings:
        print(f"{user_id}\t{movie_title}\t{rating}")
