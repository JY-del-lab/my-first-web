user_info = ["홍길동", 25, "서울"]

print(user_info[0])
print(user_info[2])

# 조건문(if) : 주방장의 상황 판단
print(" ")
print("조건문 if 시작")
age = 25

if age >= 20:
    print("성인입니다. 웹사이트 입장을 허용합니다.")
else:
    print("미성년자입니다. 접근 불가!")
print("조건문 if 끝")
print("* 파이썬의 절대 규칙(들여쓰기) if나 else: 에서 들여쓰기(Tab 또는 스페이스 4칸)을 기준으로 조건문의 포함되 코드인지 아닌지 구별함")

# 반복문(for) : 자동 조리 기계
print(" ")
print("반복문 for 시작"+"\n")
#회원 이름이 담긴 리스트 상자
members = ["이순신", "홍길동", "임꺽정"]
# members 상자에서 이름을 한 명씩 꺼내서 'name' 상자에 넣으면 반복해라!
for name in members:
    print(f"안녕하세요, {name} 회원님!") 
print("\n"+"반복문 for 끝")
print("문장앞에 f를 붙이고 {변수명}을 적용주면 글자 사이에 변수 내용물을 쏙 넣을 수 있음. 이걸 'f-string'이라고 부름")

#. 딕셔너리 (Dictionary): 사전형 데이터 상자
#  앞서 배운 리스트([])가 순서대로 나열하는 상자였다면,
#  딕셔너리({})는 '이름(Key): 값(Value)'이 쌍을 이루어 저장되는 똑똑한 상자임. 
#  마치 사전에서 단어를 찾으면 뜻이 나오는 것과 같음.
print(" ")
print("딕셔너리 Dictionary 시작"+"\n")
print("딕셔너리 상자에 회원 1명의 상세 정보를 딕셔너리로 표헌")
user ={
       "name" : "이순신",
       "age" : 30,
       "city" : "서울"
       }
print("데이터를 꺼낼 때 번호(0,1)가 아니라 '이름(key)'으로 꺼냅니다.\n")
print(user["name"])
print(user["city"])
print("\n"+"현업에서 웹이나 DB로 데이터를 주고받을 때 가장 많이 쓰는 형태가 딕셔너리 구조임")

# 함수 (Function): 반복되는 코드를 묶는 조리 기구
# Example: 반복되는 코드(똑같은 연산이나 판단)를 묶어서 '함수'라는 조리 기구를 만들어 놓으면, 필요할 때마다 호출해서 쓸 수 있음.
# 이렇게 하면 반복되는 코드를 매번 새로 작성하지 않아도 되므로, 코드가 간결해지고 유지보수가 쉬워짐.
# def (Define의 약자): 함수를 정의할 때 사용하는 키워드
# def 함수명() : 블럭 으로 묶인 코드가 함수 안에 들어가게 됨. 함수명()을 호출하면 블럭 안의 코드가 실행됨.

print("함수 (Function): 반복되는 코드를 묶는 조리 기구 \n")

print("함수 정의 예제: 나이가 20세 이상이면 '성인', 아니면 '미성년자'를 반환하는 함수 정의")
def check_adult(age):
    if age >= 20:
        return "성인"
    else:
        return "미성년자"

result1 = check_adult(25)
result2 = check_adult(17)

print(result1)
print(result2)


print("리스트(List), 딕셔너리(Dictionary)와 함수(Function):예제\n")
print( "1.함수 정의 : 회원 정보를 받아 인사말을 만드러주는 기계")
def create_welcome_message(user_data):
    #user_data는 딕셔너리 상자입니다.
    name = user_data["name"]
    age = user_data["age"]
    return f" [{name}](나이: {age}세)의 가입을 환영합니다.!"

print("2.리스트 안에 딕셔너리들이 들어 있는 실제 회원 데이터 구조")
user_list =[
    {"name": "이순신", "age": 30},
    {"name": "홍길동", "age": 18},
    {"name": "임꺽정", "age": 42}   
]
print("3.반복문으로 회원 데이터 하나씩 꺼내서 함수에 전달")
for user in user_list:
    message = create_welcome_message(user)
    print(message)