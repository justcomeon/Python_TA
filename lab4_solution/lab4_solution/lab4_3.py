#_*_ Coding:euc-kr _*_

#실습1 프로그램을 수정하여 작성하시오.
#먼저 파일메뉴에서 save 먼저 하고, 다시 save as 눌러서 lab4_3.py로 저장하세요.
#입력한 값이 1보다 작은 경우 다시 입력해달라는 메시지를 출력한 후
#다시 입력 받도록 수정해보세요. (while문 사용)

import random
print '숫자를 입력하시오'

maxNumber=1
while maxNumber <= 1:
    maxNumber = raw_input()
    maxNumber = int(maxNumber)
    if maxNumber < 1:
        print '잘못입력하셨습니다. 1이상의 숫자를 다시 입력해주세요'
    if maxNumber >= 1:    
        randomNumber = random.randint(1, maxNumber)
        print '1부터 ' + str(maxNumber) + '가운데 선택된 random  number는 ' + str(randomNumber)+ '입니다.'
        break
