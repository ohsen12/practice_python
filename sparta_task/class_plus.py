class Person:
    def __init__ (self, name, age, gender):
        self.name = name
        self.age = age
        while True:                                                 #요구하는 값을 입력할 때까지 반복
            if gender not in ['male','female']:                     #사용자가 입력한 값이 male이나 female이 아니라면 if문이 참이 되어 다음을 출력한다. 
                print('잘못된 성별을 입력하셨습니다. male 또는 female을 입력하세요.')
                gender = input('성별:')                             #다시 값을 입력 받아 gender에 저장하고 다시 반복문 처음으로 돌아간다.
                continue
            else:                                                   #사용자가 입력한 값이 male이나 female 중에 있다면 사용자가 입력한 gender 값을 객체의 성별 속성에 저장해준다.
                self.gender = gender 
                break                                               #그리고 반복문을 빠져나온다.
        
    def display(self):
        return f'''이름:{self.name}, 성별:{self.gender} 
나이:{self.age}'''

    def greet(self):                                                #Person 클래스의 greet() 메서드를 정의
        if self.age <= 0:                                           #객체의 나이 속성값이 0보다 작을 때 다음을 반환
            return f'안녕, {self.name}! 아직 안 태어났구나!'
        elif 1 <= self.age < 20:
            return f'안녕, {self.name}! 미성년자구나!'               #객체의 나이 속성값이 1보다 크거나 같고 20보다 작을 때 다음을 반환
        else:                                                      #객체의 나이 속성값이 20보다 크거나 같을 때 다음을 반환
            return f'안녕하세요, {self.name}! 성인이시군요!'
        
    
p_name = input('이름:')
p_age = int(input('나이:'))
p_gender = input('성별:')

Person = Person(p_name, p_age, p_gender)


print(Person.display())                                    
print(Person.greet())       #Person 클래스로 만든 Person 객체에서 Person 클래스의 greet() 메서드를 호출하여 반환값을 출력