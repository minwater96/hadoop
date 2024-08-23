import sys

current_rating = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    rating, count = line.split("\t")
    
    try:
        count = int(count)
    except ValueError:
        continue

    if current_rating == rating:
        current_count += count
    else:
        if current_rating is not None:
            print(f"{current_rating}\t{current_count}")
        current_rating = rating
        current_count = count

if current_rating == rating:
    print(f"{current_rating}\t{current_count}")
