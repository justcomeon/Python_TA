#
# while ����
import random
import time

print '����� ���õ� ������ ������ ���ϴ�.'
print

meetTheBear=random.randint(1,10)
axingCount = 0
while axingCount < 10:
    axingCount = axingCount + 1
    print '������ '+str(axingCount)+'�� ������ϴ�.'
    time.sleep(2)
    if meetTheBear == axingCount:
        break

print '������ ��� �� \n ����� ū ���� �����ϴ�!!! '
time.sleep(1.2)
print 
print '���� ĥ���? (1) or �ο���?(2)'


answer = raw_input()
answer = int (answer)

if answer == 1:
    print '��~~~~~~~���� �������� ���!!!'
    time.sleep(2)
    print '����� �Ѿư��� ��!!!'
    time.sleep(2)

    running=0
    while running<5:
        print '�� '*running +' �����پ�!'
        print '...' 
        time.sleep(1)
        running=running+1

    print '........'        
    con = random.randint(0,1)
    if con == 0:
        print '��~ ����� ������ �����ƽ��ϴ�! '
    if con == 1:
        print '���ƾƾƾƾƾ�~! ���� �������!�Ф�'

if answer == 2:
    print '����� 7���� ���� �ȿ� ���� �����ľ� �մϴ�.'
    #print '�� ���� ���� ���ڰ� ������ �������� 3�谡 �˴ϴ�.'
    time.sleep(2)
    Mon = 50
    cnt = 0
    MaxDam = 15
    while cnt < 7 :
        hit1 = random.randint(0, MaxDam)
        print
        cnt = cnt + 1
        print str(cnt)+'��° ����!!'                
        print str(cnt)+'��° ����� �������� ���� ' + str(hit1) + '�� ���ظ� �Ծ����ϴ�.'
        Mon = Mon - hit1
        
        if Mon < 0:
            print '���� �����ƴ�!!'
            break
        
        print '���� ���� ü���� ' + str(Mon) + '�Դϴ�.'
        time.sleep(3)

        
    print
    
    if Mon < 0 :
        print '�¸���!!! �������� ������ϴ�.'
    if Mon > 0:
        print '���ƾ�!'
            

