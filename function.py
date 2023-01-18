def func1():
    print('func1 시이작')
#함수 안에도 또 쓸수 있다?
    def func2():
        print('func2 시이작')
        print('func2 끝')
        return

    func2()
    return

func1() #<< 함수 호출해줘야 실행함
##################################################
x = '글로벌' #<< 이 x는 글로벌에 존재

def func1():

    def func2():
        print(x) #<< local 부분 없어

    func2()


func1()
#####################################
def en():
    a = 10

    def lo(a):
        print(a)
        lo(300)


######################################
# # 아래에 답안을 작성해 주세요.
