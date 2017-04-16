#_*_ Coding:euc-kr _*_


#실습 1
#사용자로부터 숫자를 입력 받아 1부터 입력한 숫자까지를 범위로 하여
#random 값을 출력하는 프로그램을 작성하여 lab4_1.py로 저장하시오.


import random
print '숫자를 입력하시오'

maxNumber=0
while maxNumber < 1:
    maxNumber = raw_input()
    maxNumber = int(maxNumber)
    if maxNumber >= 1:    
        randomNumber = random.randint(1, maxNumber)
        print '1부터 ' + str(maxNumber) + '가운데 선택된 random  number는 ' + str(randomNumber)+ '입니다.'

