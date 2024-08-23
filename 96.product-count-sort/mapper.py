import sys
import re

# 정규 표현식을 사용해 /product/:product_id 형식의 URL에서 product_id를 추출
product_pattern = re.compile(r'/product/(\d+)')

# 표준 입력에서 로그 데이터를 읽음
for line in sys.stdin:
    parts = line.strip().split(' ')
    
    if len(parts) > 6:
        url = parts[6]  # URL 부분은 로그에서 7번째 요소에 위치
        
        match = product_pattern.search(url)
        if match:
            product_id = match.group(1)
            print(f"{product_id}\t1")  # product_id와 함께 1을 출력
