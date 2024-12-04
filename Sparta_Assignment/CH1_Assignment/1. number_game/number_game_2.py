from random import randint #random 모듈에서 지정된 범위에서 하나의 난수를 반환하는 randint 함수를 불러온다. (지정범위의 끝값을 반영함)

computer = randint(1,10)   #1-10 범위의 난수 하나 생성
while True:                                                             
    player = int(input('숫자를 입력하세요. 0를 입력하면 종료합니다. :'))  
    if player == 0:                                                       
        print('0을 입력하여 종료합니다.')
        break
    if player > 10:                                                  #플레이어가 10을 벗어난 숫자를 입력하면 반복문을 다시 시작한다.
        print('1부터 10까지의 숫자만 입력하세요.')
        continue
    if player - computer == 1 or computer - player == 1:             #1의 오차범위가 났을 때에만 정말 가깝다고 알려준다. 
        print('정말 가깝습니다!')
    elif player > computer:                                              
        print('입력한 숫자가 더 큽니다.')
    elif player < computer:
        print('입력한 숫자가 더 작습니다.')                                
    else:                                                            #정답을 맞힌 경우 게임을 다시 시작할 것인지 물어본다.                        
        print('정답입니다!')
        restart = input ('''게임을 다시 시작하시겠습니까?                 
Y 또는 N 으로 대답하세요.''')
        restart = restart.lower()                                    #소문자로 입력해도 반영되도록 문자열의 lower() 메서드를 호출해서 저장해준다.
        if restart == 'y':
            computer = randint(1,10)                                 #대답이 Y이면 새로운 난수를 생성하고 반복문을 다시 시작한다.
            continue
        elif restart == 'n':
            print('종료합니다.')                                      #대답이 N이면 반복문을 종료한다.
            break 