import sys

current_product_id = None
current_count = 0
product_counts = {}

# 표준 입력에서 Mapper의 출력을 읽음
for line in sys.stdin:
    product_id, count = line.strip().split('\t')
    count = int(count)

    if current_product_id == product_id:
        current_count += count
    else:
        if current_product_id:
            product_counts[current_product_id] = current_count
        current_product_id = product_id
        current_count = count

# 마지막 product_id 처리
if current_product_id:
    product_counts[current_product_id] = current_count

# 등장 빈도순으로 정렬하여 출력
sorted_products = sorted(product_counts.items(), key=lambda x: x[1], reverse=True)

for product_id, count in sorted_products:
    print(f"{product_id}\t{count}")
