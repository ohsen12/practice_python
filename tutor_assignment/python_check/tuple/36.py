# 숙제 - 36
# 리스트 [11, 22, 33, 44]에 11의 값을 110으로 변경
# 튜플 (11, 22, 33, 44)에 11의 값을 110 변경 시도 

l = [11, 22, 33, 44]
t = (11, 22, 33, 44)

l[l.index(11)] = 110
# 튜플은 불변 자료형이라 튜플에서 바로 인덱스 값을 수정하는 건 안된다.

# 튜플은 리스트로 바꿔서 해당 인덱스 값을 수정해주고 다시 튜플로 바꾸면 된다.
t = list(t)
t[t.index(11)] = 110
    

print(l,tuple(t)) # 의도하신 정답이 이게 맞나..