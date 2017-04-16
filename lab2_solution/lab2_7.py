#다음과 같이 동작하는 프로그램을 lap2_7.py로 작성하시오.

# print문과 raw_input문을 아래와 같이 각각 입력해도 됨
print 'Tell me what your name is.'
name= raw_input()

# raw_input문 괄호안에 출력문장을 입력해도 됨
nationality = raw_input('Tell me what your nationality is.')
destination = raw_input('Tell me where will you go.')
transportation = raw_input('Tell me how will you go.')
purpose = raw_input('Tell me what purpose of travel.')
hotel = raw_input('Tell me where you stay in.')
lengthOfStay = raw_input('Tell me how long will you stay.')

print 'You entered: ' + name + ' ' + nationality + ' ' + destination + ' '+ transportation + ' ' + purpose+ ' ' + hotel +' ' +lengthOfStay

print 'Name: ' + name
print 'Nationality: ' + nationality
print 'Destination: ' + destination
print 'Transportation: ' + transportation
print 'Purpose: ' + purpose
print 'Hotel: ' + hotel
print 'lengthOfStay: ' + lengthOfStay
