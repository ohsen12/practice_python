import pandas as pd 

#데이터 불러오기
df = pd.read_excel(r'/Users/t2023-m0045/Desktop/Assignment/Sparta_Assignment/CH1_Assignment/3. library/data/관서별 5대범죄 발생 및 검거.xlsx') 

mapping_dict = {
                '서대문서': '서대문구', '수서서': '강남구', '강서서': '강서구', '서초서': '서초구',
'서부서': '은평구', '중부서': '중구', '종로서': '종로구', '남대문서': '중구',
'혜화서': '종로구', '용산서': '용산구', '성북서': '성북구', '동대문서': '동대문구',
'마포서': '마포구', '영등포서': '영등포구', '성동서': '성동구', '동작서': '동작구',
'광진서': '광진구', '강북서': '강북구', '금천서': '금천구', '중랑서': '중랑구',
'강남서': '강남구', '관악서': '관악구', '강동서': '강동구', '종암서': '성북구', 
'구로서': '구로구', '양천서': '양천구', '송파서': '송파구', '노원서': '노원구', 
'방배서': '서초구', '은평서': '은평구', '도봉서': '도봉구'
               }

#데이터 매핑하고 결측값은 '구 없음'으로 채워주기
df['구별'] = df['관서명'].map(mapping_dict).fillna('구 없음')

#피벗테이블 생성하기
pivot = pd.pivot_table(df, index = '구별', 
                       values =['소계(발생)', '소계(검거)', '살인(발생)',
                                '살인(검거)', '강도(발생)', '강도(검거)',
                                '강간(발생)', '강간(검거)', '절도(발생)',
                                '절도(검거)', '폭력(발생)', '폭력(검거)'],
                       aggfunc = 'sum')

#'구 없음' 행 탈락시키기
pivot.drop(index = '구 없음', inplace = True)

#검거율 컬럼 생성하기
crime_list = ['강간','강도','살인','절도','폭력']
for crime in crime_list:                          
    pivot[f'{crime}검거율'] = (pivot[f'{crime}(검거)'] / pivot[f'{crime}(발생)']) *100    

#총검거율 컬럼 생성하기
arrests = pivot['소계(검거)'] 
cases = pivot['소계(발생)']
pivot['검거율'] = (arrests / cases) *100  #각 행 (구별) 총 검거율

#필요없는 컬럼 지우기
del pivot['소계(발생)']
del_list = ['강간','강도','살인','절도','폭력','소계']
for crime in del_list:
    del pivot[f'{crime}(검거)']

#컬럼명 변경하기
pivot.rename(columns = {'강간(발생)':'강간',
'강도(발생)':'강도',
'살인(발생)':'살인',
'절도(발생)':'절도',
'폭력(발생)':'폭력' }, inplace = True)

#추가 도전 과제

pop = pd.read_csv('/Users/t2023-m0045/Desktop/Assignment/Sparta_Assignment/CH1_Assignment/3. library/data/pop_kor.csv', index_col='구별')  #pandas를 사용해 데이터를 불러오는데 인덱스를 '구별'로 설정한다.
print(pop.head())

print() #실행결과 볼 때 가독성을 위해 추가함

#인덱스를 기준으로 데이터프레임을 병합하기 위해 join() 사용. 이미 둘다 인덱스가 '구별'이므로 set_index('컬럼명') 해줄 필요 없다.
joined_df = pivot.join(pop)

sorted_df = joined_df.sort_values(by = '검거율') #검거율 열의 데이터를 기준으로 오름차순 정렬

print(sorted_df.head()) #5행까지만 보겠음