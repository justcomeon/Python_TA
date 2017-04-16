#_*_ Coding:euc-kr _*_

#실습 4-4
#올바른 암호를 입력할 때까지 입력 받아 암호가 올바르게 입력되면
#로그인 성공이라는 메시지를 출력하는 프로그램을 작성하세요.


password =''
while password != 'pythonisfun':
    password = raw_input('비밀번호를 입력하세요: ')
print '로그인 성공'
