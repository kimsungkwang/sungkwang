# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

n = int(input())

total = 0  # 변수에 0을 지정
for i in range(1, n+1) :  # 1부터 n까지
    total += i  # total = total + i와 같은 의미
print(total)