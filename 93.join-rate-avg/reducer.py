import sys

current_movie_id = None
current_movie_name = None
current_rating_sum = 0
current_rating_count = 0

# 각 키에 대해 처리
for line in sys.stdin:
    line = line.strip()
    parts = line.split('\t')
    
    if len(parts) == 3:
        movie_id, source, value = parts
        
        if source == "data":
            # 평점 처리
            try:
                rating = float(value)
            except ValueError:
                continue
            
            if current_movie_id == movie_id:
                current_rating_sum += rating
                current_rating_count += 1
            else:
                # 이전 영화의 평균 평점 출력
                if current_movie_id and current_movie_name:
                    avg_rating = current_rating_sum / current_rating_count
                    print(f"{current_movie_name}\t{avg_rating:.2f}")
                
                # 새로운 영화로 초기화
                current_movie_id = movie_id
                current_rating_sum = rating
                current_rating_count = 1
        
        elif source == "item":
            # 영화 이름 처리
            if current_movie_id == movie_id:
                current_movie_name = value
            else:
                if current_movie_id and current_movie_name:
                    avg_rating = current_rating_sum / current_rating_count
                    print(f"{current_movie_name}\t{avg_rating:.2f}")
                
                current_movie_id = movie_id
                current_movie_name = value
                current_rating_sum = 0
                current_rating_count = 0

# 마지막 영화 처리
if current_movie_id and current_movie_name:
    avg_rating = current_rating_sum / current_rating_count
    print(f"{current_movie_name}\t{avg_rating:.2f}")
