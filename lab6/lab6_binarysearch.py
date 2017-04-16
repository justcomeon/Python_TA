#이진 탐색 알고리즘
#_*_coding:euc-kr_*_
import random

#number =random.randint(1, 1000)
print '학번:2017000000, 이름:김아무개, 학과:본인학과'
print
print '1부터 1000가운데 검색하고자 하는 숫자를 입력하세요.'
number=raw_input()
number = int(number)
start = 1
end = 1000
count=0
myGuess=0
while myGuess != number:
    myGuess = (start+end)/2
    count=count+1    
    print '추측값: ', myGuess, '검색횟수:', count    
    if myGuess < number:
        start = myGuess+1
    if myGuess > number:
        end = myGuess-1

print count,'번 만에 찾았습니다'


