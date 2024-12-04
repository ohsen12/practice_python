from random import choice   #random 모듈의 choice 함수는 주어진 시퀀스에서 무작위로 하나의 요소를 선택해서 반환한다.

num_list = range(1,11)      #숫자시퀀스를 반환하는 range 함수를 통해 1-10까지의 숫자 시퀀스를 만든다.
computer = choice(num_list) #컴퓨터가 숫자시퀀스에서 고른 난수

while True:                                                       #0을 입력하거나 정답을 맞힐 때까지 프로그램을 계속한다.
    player = int(input('숫자를 입력하세요. 0를 입력하면 종료합니다. :'))    #input 함수는 문자열을 반환하므로 int로 바꿔준다.
    if player == 0:                                               #0를 입력하면 프로그램을 종료한다.
        print('0를 입력하여 종료합니다.')
        break
    elif player > computer:                                       #사용자가 입력한 수가 더 클 때
        print('입력한 숫자가 더 큽니다.')
    elif player < computer:
        print('입력한 숫자가 더 작습니다.')                              #사용자가 입력한 숫자가 더 작을 때
    else:                                                          #위의 모든 조건이 False라면 두 수가 같아 정답을 맞춘 것이므로 break를 사용하여 반복문 종료.
        print('정답입니다!')
        break 
    



