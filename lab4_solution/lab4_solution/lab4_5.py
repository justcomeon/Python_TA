#_*_ Coding:euc-kr _*_

#실습4-5
#원하는 단을 입력 받아 그 단의 구구단을 출력하는 프로그램을 while문을 이용하여 작성하세요.

dan = raw_input('원하는 단은:')
num=1
dan = int(dan)
while num<=dan:
    print str(dan)+'*'+str(num)+'='+str(num*dan)
    # 아래와 같이도 표현할 수 있어요.
    # print ("%s*%s=%s" %(dan, num, dan*num))
    num=num+1
