#���� Ž�� �˰���
#_*_coding:euc-kr_*_
import random

#number =random.randint(1, 1000)
print '�й�:2017000000, �̸�:��ƹ���, �а�:�����а�'
print
print '1���� 1000��� �˻��ϰ��� �ϴ� ���ڸ� �Է��ϼ���.'
number=raw_input()
number = int(number)
start = 1
end = 1000
count=0
myGuess=0
while myGuess != number:
    myGuess = (start+end)/2
    count=count+1    
    print '������: ', myGuess, '�˻�Ƚ��:', count    
    if myGuess < number:
        start = myGuess+1
    if myGuess > number:
        end = myGuess-1

print count,'�� ���� ã�ҽ��ϴ�'


