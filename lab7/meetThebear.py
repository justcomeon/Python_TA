#
# while 연습
import random
import time

print '당신은 오늘도 나무를 찍으러 갑니다.'
print

meetTheBear=random.randint(1,10)
axingCount = 0
while axingCount < 10:
    axingCount = axingCount + 1
    print '나무를 '+str(axingCount)+'번 찍었습니다.'
    time.sleep(2)
    if meetTheBear == axingCount:
        break

print '나무를 찍던 중 \n 당신은 큰 곰을 만납니다!!! '
time.sleep(1.2)
print 
print '도망 칠까요? (1) or 싸울까요?(2)'


answer = raw_input()
answer = int (answer)

if answer == 1:
    print '열~~~~~~~심히 도망가는 당신!!!'
    time.sleep(2)
    print '당신을 쫓아가는 곰!!!'
    time.sleep(2)

    running=0
    while running<5:
        print '더 '*running +' 빨리뛰어!'
        print '...' 
        time.sleep(1)
        running=running+1

    print '........'        
    con = random.randint(0,1)
    if con == 0:
        print '휴~ 당신은 무사히 도망쳤습니다! '
    if con == 1:
        print '으아아아아아악~! 곰이 빨랐어요!ㅠㅠ'

if answer == 2:
    print '당신은 7번의 공격 안에 곰을 물리쳐야 합니다.'
    #print '두 명이 같은 숫자가 나오면 데미지는 3배가 됩니다.'
    time.sleep(2)
    Mon = 50
    cnt = 0
    MaxDam = 15
    while cnt < 7 :
        hit1 = random.randint(0, MaxDam)
        print
        cnt = cnt + 1
        print str(cnt)+'번째 공격!!'                
        print str(cnt)+'번째 당신의 공격으로 곰이 ' + str(hit1) + '의 피해를 입었습니다.'
        Mon = Mon - hit1
        
        if Mon < 0:
            print '곰을 물리쳤다!!'
            break
        
        print '곰의 남은 체력은 ' + str(Mon) + '입니다.'
        time.sleep(3)

        
    print
    
    if Mon < 0 :
        print '승리☆!!! 곰가죽을 얻었습니다.'
    if Mon > 0:
        print '으아악!'
            

