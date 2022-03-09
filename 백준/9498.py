# 시험 점수를 입력받아 
# 90 ~ 100점은 A, 
# 80 ~ 89점은 B, 
# 70 ~ 79점은 C, 
# 60 ~ 69점은 D, 
# 나머지 점수는 F
# 를 출력하는 프로그램을 작성하시오.

score = int(input())    #시험점수 입력

if score>=90:   # 만약 시험점수가 90점이상이면 에이
    print('A')
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("F")
