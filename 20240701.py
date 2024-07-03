# 주석comment : 번역 되지 않는 영역. 한줄 주석
#          기계어로 번역 되지 않으므로 참고사항 작성 

'''
   여러줄 주석. 여러줄 문자열 변수로도 사용됨   
'''

"""
여러줄 주석. 여러줄 문자열 변수로도 사용됨
"""
#[shift]+[enter] => 현재 라인 실행 
#[shift]+[enter] => 선택된 라인 실행
print("\"안녕하세요\"라고 말했습니다."); 

#문자열
print("hello")
print(len("hello")) #len : 문자열의 길이 리턴 함수
print(type("hello"))

print("안녕"*3)
print("안녕"+"하세요")
print("학번:"+1000) #오류 발생 str+str끼리만 +연산 가능
print("학번:"+"1000") 
print("학번:"+str(1000)) #str(데이터) => 데이터를 문자열로 변경

a=10
print(a)
a+=10
print(a)  #20

a*=2
print(a)  #40

a -= 15
print(a)
a -= 15
print(a)

a = int(input("숫자를 입력하세요:"))  #a : int(str 형) : 정수형으로 형변환 함수
print(a + 100)                 # str + 숫자 => 오류 
'''
문자열[1:3] : 1번인덱스(두번째문자)부터 3번인덱스(네번째) 앞까지.
         => 1,2 인덱스 까지의 부분문자열
'''
print("0123456"[1:3])  #12

#inch 단위를 입력받아 cm 단위로 출력하기
# 1 inch = 2.54 cm
inch = float(input("inch를 입력하세요"))
print(inch,":",inch*2.54,"cm")

# 진수 변경하기
sel = int(input("입력 진수 결정(16/10/8/2) : "))
num = input("값 입력 : ") #11
num10 = int(num,16)  #11 16진수로 인식. 
print(num10) # 17
num10 = int(num,10)  #기본은 10진수
print(num10) #11
num10 = int(num,8) 
print(num10) #9
num10 = int(num,2)
print(num10) #3
# if 조건문
'''
   if 조건문 :
      구문   => 조건문의 결과가 참인 경우만 실행
  == : 등가연산자 
  sel == 16 => sel 값이 16인 경우 결과가 참.    
'''
if sel == 16 :
    num10 = int(num,16)
if sel == 10 :
    num10 = int(num,10)    
if sel == 8 :
    num10 = int(num,8)        
if sel == 2 :
    num10 = int(num,2)            
print(num10) #10진수 출력

#10진수 를 16,8,2 진수 변경하여 출력하기
print("16진수=>",hex(15)) #0xf
print("8진수=>",oct(10))  #0o12
print("2진수=>",bin(10))  #0b1010

# print 함수 : 콘솔(화면) 출력
a=10
b=20
#print("a="+a) #str + int 형의 + 연산 불가
print("a=",a)
#a=10,b=20,a+b=30 => 출력하기
print("a=",a,",b=",b,",a+b=",a+b)
print("a=%d,b=%d,a+b=%d" % (a,b,a+b))
print(f"a={a},b={b},a+b={a+b}") #변수값을 직접 출력
print("a={0:d},b={1:d},a+b={2:d}".format(a,b,a+b))
print("a={2:d},b={1:d},a+b={0:d}".format(a+b,b,a))
print("안녕하세요", end="=>")
print("홍길동 입니다.")