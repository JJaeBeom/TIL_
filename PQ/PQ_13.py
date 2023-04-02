# 16진수 1자리는 2진수 4자리로 표시
# N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램을 만드시오
# 단, 2진수의 앞자리 0도 반드시 출력한다
# ex) 47FE라는 16진수를 2진수로 표시하면 다음과 같다
# 0100011111111110
'''
3
4 47FE
5 79E12
8 41DA16CD
'''

T = int(input())
for tc in range(1, T+1):
    N, Hex = input().split()
    A = int(Hex,16)
    # print(hex(A))
    print(f'#{tc} {A:b}')

# 정식이 은행 업무
# T = int(input())
# for tc in range(1, T+1):
#     Bin = input()
#     Mul = input()
    
#     Bin_list = []
#     for i in range(len(Bin)):
#         if Bin[i] == '0':
#             Bin1= Bin[:i] + '1' + Bin[i+1:]
#             Bin_list.append(int(Bin1, 2))
#         else:
#             Bin1= Bin[:i] + '0' + Bin[i+1:]
#             Bin_list.append(int(Bin1, 2))
    
#     Mul_list = []
#     for j in range(len(Mul)):
#         if Mul[j] == '0':
#             Mul1 = Mul[:j] + '1' + Mul[j+1:]
#             Mul_list.append(int(Mul1, 3))
#             Mul1 = Mul[:j] + '2' + Mul[j+1:]
#             Mul_list.append(int(Mul1, 3))
#         elif Mul[j] == '1':
#             Mul1 = Mul[:j] + '0' + Mul[j+1:]
#             Mul_list.append(int(Mul1, 3))
#             Mul1 = Mul[:j] + '2' + Mul[j+1:]
#             Mul_list.append(int(Mul1, 3))
#         else:
#             Mul1 = Mul[:j] + '0' + Mul[j+1:]
#             Mul_list.append(int(Mul1, 3))
#             Mul1 = Mul[:j] + '1' + Mul[j+1:]
#             Mul_list.append(int(Mul1, 3))
#     for x in range(len(Bin_list)):
#         if Bin_list[x] in Mul_list:
#             print(f'#{tc} {Bin_list[x]}')

###############################################################
# Q1. T(n) = T(n-1) + 1 , T(0) = 1
            T(n-1-1)+1 + 1
#     T(n) = (T(n-2)+1)+1
#     T(n) = ((T(n-3)+1)+1)+1
#          = 1 + 1+ 1+ 1+ 1
#          = n+1
#         => O(n)
Q2. T(n) = T(n-1) + n , T(0) = 1
    T(n) = T(n-2) + n - 1 + n 
    T(n) = T(n-3) + n - 2 + n - 1 + n

    O(n^2)