import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split("\t")  # 필드를 탭(\t)으로 분리
    if len(fields) == 4:
        rating = fields[2]  # 평점 필드 추출
        print(f"{rating}\t1")  # 평점별로 1씩 출력
