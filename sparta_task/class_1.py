class Person:                                            #Person 클래스 정의 시작
    def __init__ (self, age, name, gender):              #객체의 초기화를 담당할 생성자 메서드. self에는 객체자신을 받으며 Person 클래스를 호출할 때 이름, 성별, 나이를 받아 속성을 초기화한다. 
        self.name = name                                 #입력받은 나이,이름,성별을 객체의 나이,이름,성별 속성으로 저장한다.
        self.gender = gender
        self.age = age
    
    def display(self):                                  #Person 클래스에 display 라는 메서드를 정의. 사용자에게 입력받아 저장한 객체의 속성을 불러와서 사용자의 이름, 성별, 나이를 반환한다.
        return f'''이름:{self.name}, 성별:{self.gender}  
나이:{self.age}'''

p_age = int(input('나이:'))                             #input 함수는 str을 반환하기 때문에 정수화해준다. (정수화를 하지 않아도 최종 결과도출에는 영향을 안 미치긴 한다.)
p_name = input('이름:')                                 #사용자의 나이,이름,성별을 입력받아 저장할 변수를 생성
p_gender = input('성별:')                             

Person = Person(p_age, p_name,p_gender)                  #Person 클래스를 사용하여 Person이라는 객체 생성. 사용자가 입력한 정보를 클래스의 인자로 넣어준다.

print(Person.display())                                 #객체는 클래스의 속성과 메서드를 공유하므로, 해당 객체에 display() 메서드를 불러와 반환값을 출력한다.