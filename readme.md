# MR

- mapreduce 개념

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/6324d94a-8672-4ce8-912c-5d35141f904c/39e7f8dd-e8d9-491a-bdb2-544192725b3a/image.png)

## word count

- text.txt

```bash
apple hello
world apple hello
world apple hello
apple hello hello hello
world apple apple
world
apple hello hello
world apple
world apple
```

- mapper.py

```python
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()

    for word in words:
        print(f'{word}\t1')
```

- reducer.py

```python
import sys

last_word = None
total_count = 0

for line in sys.stdin:
    line = line.strip()

    word, value = line.split('\t')
    value = int(value)

    if last_word == word:
        total_count += value
    else:
        if last_word is not None:
            print(f'{last_word}\t{total_count}')
        last_word = word
        total_count = value

if last_word == word:
    print(f'{last_word}\t{total_count}')
```

- linux 환경에서 실행

```bash
cat test.txt | python3 mapper.py | sort | python3 reducer.py
```

---

- requestly 설치
    - replace url 설정
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/6324d94a-8672-4ce8-912c-5d35141f904c/f733e561-d47a-496d-874c-bdf54f177a29/image.png)
    

- 파일 확인

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/6324d94a-8672-4ce8-912c-5d35141f904c/81fd39ff-76b1-42df-aea9-f6a48af7a9b8/image.png)

---

- hadoop으로 MR job 실행

```bash
hadoop jar ~/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-input /user/ubuntu/input/test.txt \
-output /user/ubuntu/output/wordcount \
-mapper 'python3 /home/ubuntu/dmf/hadoop/0.wordcount/mapper.py' \
-reducer 'python3 /home/ubuntu/dmf/hadoop/0.wordcount/reducer.py'
```

---

## Movie lens

https://grouplens.org/datasets/movielens/

- MovieLens 100K Dataset

- 영화별 평점 조회

```bash
hadoop jar ~/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-input /user/ubuntu/input/u.data \
-output /user/ubuntu/output/movie-avg \
-mapper 'python3 /home/ubuntu/dmf/hadoop/1.movie-rate-avg/mapper.py' \
-reducer 'python3 /home/ubuntu/dmf/hadoop/1.movie-rate-avg/reducer.py'
```

- 시간별 로그데이터

```bash
hadoop jar ~/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-input /user/ubuntu/input/access.log \
-output /user/ubuntu/output/log-time \
-mapper 'python3 /home/ubuntu/dmf/hadoop/2.log-time/mapper.py' \
-reducer 'python3 /home/ubuntu/dmf/hadoop/2.log-time/reducer.py'
```