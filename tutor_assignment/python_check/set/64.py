# 숙제 - 64
# {1, 2, 3, 4}와, {3, 4, 5, 6}의 합집합 출력

# set(집합) 자료형은 다양한 집합 연산을 제공한다.
# 합집합 : 메서드 union() 또는 |
# 교집합 : 메서드 intersection() 또는 &
# 차집합 : 메서드 difference() 또는 -

print({1, 2, 3, 4}|{3, 4, 5, 6}) # 중복을 허용하지 않는 셋 자료형이기 때문에 합쳐지면서 중복요소는 제거된다.