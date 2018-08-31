
**문제**    
2 x n 타일링 (level 3)

문제 설명   

가로 길이가 2이고 세로의 길이가 1인 직사각형모양의 타일이 있습니다. 이 직사각형 타일을 이용하여 세로의 길이가 2이고 가로의 길이가 n인 바닥을 가득 채우려고 합니다. 타일을 채울 때는 다음과 같이 2가지 방법이 있습니다.   

- 타일을 가로로 배치 하는 경우   
- 타일을 세로로 배치 하는 경우   

예를들어서 n이 7인 직사각형은 다음과 같이 채울 수 있습니다.   

ㅣㅡㅡㅣㅣㅡㅡ   
ㅣㅡㅡㅣㅣㅡㅡ   

직사각형의 가로의 길이 n이 매개변수로 주어질 때, 이 직사각형을 채우는 방법의 수를 return 하는 solution 함수를 완성해주세요.   

제한사항.  
가로의 길이 n은 60,000이하의 자연수 입니다.   
경우의 수가 많아 질 수 있으므로, 경우의 수를 1,000,000,007으로 나눈 나머지를 return해주세요.   

<br>

[접근]   
1. 피보나치 수열과 비슷한 규칙성이 있으리라 생각했고, 메모이제이션과 bottom-up을 이용한 규칙성을 찾아보려고 했다.
2. 먼저 메모이제이션과 bottom-up 연습을 위해 대략 예상되는 규칙을 적용하여 코드를 작성해봤다. 그러나 역시나 정답은 아니었다. (solution_1 & solution_2)
3. 규칙은 생각보다 간단했다. 선행되는 두 원소를 더하면 다음 후행되는 원소가 되는 구조였다.
	- 메모이제이션과 bottom-up 그리고 파이썬에서 가능한 트릭을 이용해서 좀 더 간결하게 코드를 짰다. (solution_3)
    - 계산 시간을 조금 줄여보기위해 약간 코드를 바꿔서, iteration의 길이를 줄여봤다.(solution_final)


```python
def solution_1(n):
    memo = [None] * (n-1)
    memo[0], memo[1] = 1, 1
    for i in range(2,  n-1):
        memo[i] = memo[i-2] + memo[i-1]
    return 1+sum(memo)%1000000007
```


```python
def solution_2(n):
    lst = [0,1,2]
    for i in range(3, n+1):
        lst.append(lst[i-1]+lst[i-2])
    return lst[n]%1000000007
```


```python
def solution_3(n):
    lst = [1,2]
    for i in range(2, n+1):
        lst[0], lst[1] = lst[1], lst[0]+lst[1]
    return lst[0]%1000000007
```


```python
def solution_final(n):
    lst = [1,2]
    for _ in range(n-2):
        lst[0], lst[1] = lst[1], lst[0]+lst[1]
    return lst[1]%1000000007

if __name__ == "__main__":
    print(solution_final(3))
    print(solution_final(5))
    print(solution_final(10))
```

    3
    8
    89


문제 출처
- https://programmers.co.kr/learn/courses/30/lessons/12900
