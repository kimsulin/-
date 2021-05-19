# 이름과 나이를 받아라
# 나이가 20 미만이면 "안녕"이라고 
# 나이가 21 살에서 30 살 사이면 "안녕하세요"라고
# 그 외에는 "안녕하십니까"라고 말해라

def  sayHello ( name , age ) :                 # 이름과 나이를 인자로 포함.
    if  age  <  20 :                         # 나이가 20보다 작 으면
        print ( "안녕,"  +  name )           # 안녕이라고 출력해라
    elif  age  <= 21  and  age  > =  30 :         # 나이가 20 살보다 적고 30 살보다 크면
        print ( "안녕하세요,"  +  name )     # 안녕하세요.
    else :                                # 그외에는
        print ( "안녕하십니까,"  +  name )   #
        
sayHello ( "태희" , 15 )
sayHello ( "정수" , 7 )
sayHello ( "세영" , 35 )
sayHello ( "철수" , 24 )