print '두 정수를 입력하세요'
num1 = raw_input()
num2 = raw_input()

if int(num1) < int(num2):
    print '큰수: ' + num2
    print '작은수: ' + num1
if int(num1) > int(num2):
    print '큰수: ' + num1
    print '작은수: ' + num2
if int(num1) == int(num2):
    print '두 수는 같습니다'
