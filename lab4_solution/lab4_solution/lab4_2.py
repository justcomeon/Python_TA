#_*_ Coding:euc-kr _*_

#실습 4-2
#1~100까지 숫자를 더해 합을 출력하는 프로그램을 while문을 사용하여 작성한 후
#lab4_2.py로 저장하시오.
#1. 변수가 몇 개 필요한지를 생각한다. 
#2. while문에서 조건을 어떻게 줄 것 인지를 생각한다. 

num =1
total = 0
while num<=100:
    total = total + num
    num = num + 1
print '1부터 100까지의 합계는 ' + str(total) + '입니다'
