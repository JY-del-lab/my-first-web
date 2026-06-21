# 1. 3명의 나이가 담긴 리스트(List) 변수 생성
age_list = [18, 25, 15]

# 2. 반복문(for)으로 나이를 한 명씩 꺼내기
for age in age_list:
    # 3. 조건문(if)으로 20세 이상인지 판단하기
    if age >= 20:
        print(f"나이 {age}세: 성인인증 성공!")
    else:
        print(f"나이 {age}세: 미성년자입니다.")