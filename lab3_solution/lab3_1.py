#두 개의 정수를 입력 받아 덧셈 연산을 실행한 후에,
#연산 결과를 화면에 출력하는 프로그램을 작성하시오. (lab2_8.py)


#_*_ coding: euc-kr _*_

#방법1
num1=raw_input('첫 번째 정수를 입력하시오:')
num2=raw_input('두 번째 정수를 입력하시오:')
print num1+'과 '+num2+'의 합은',
print int(num1)+int(num2),
print '입니다'

#방법2
num1=raw_input('첫 번째 정수를 입력하시오:')
num2=raw_input('두 번째 정수를 입력하시오:')
sum = int(num1)+int(num2)
print num1+'과 '+num2+'의 합은'+str(sum)+'입니다'
#str은 아직 배우지 않았어요~

#방법3
num1=raw_input('첫 번째 정수를 입력하시오:')
num2=raw_input('두 번째 정수를 입력하시오:')
sum = int(num1)+int(num2)
print num1,'과',num2,'의 합은',sum,'입니다.'


