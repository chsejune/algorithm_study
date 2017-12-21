__author__ = 'Sejune Cheon'

"""
상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.

상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.

상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.
"""
#
# # 입출력
# kg = int(input())
#
# d5 = kg//5 # 몫 저장
# r5 = kg%5 # 나머지 저장
#
# if r5==0: # 나머지가 0 이면 몫 출력
#     print('{}'.format(d5))
# elif r5 !=0: # 나머지가 0이 아니면
#     d3 = r5//3 # 몫 저장
#     r3 = r5%3 # 나머지 저장
#     if r3==0: # 나머지가 0이면
#         print('{}'.format(d5+d3)) # 몫 출력
#     else:
#         print('{}'.format(-1)) # -1 출력
#
#
# ## init count
# d5_count = kg//5
#
# d3_count = (kg%5)//3
#
# if (5*d5_count+3*d3_count)==kg:
#     print(d5_count+d3_count)
# else:
#     d5_count-=1
#     d3_count = (kg-5*d5_count)//3
#
#

kg = int(input())


kg = 18

d5_count = kg//5

d3_count = (kg%5)//3

# while (5*d5_count+3*d3_count)!=kg:
flag=True
while flag == True:
    if d5_count<0:
        print(-1)
        break
    elif (5*d5_count+3*d3_count)==kg:
        print(d5_count+d3_count)
        break
    d5_count -= 1
    d3_count = (kg - 5 * d5_count) // 3



# def go(N):
#     if (5-(N%5))%2 == 0:
#         b = (5-(N%5))/2
#         a = (N-3*b)/5
#     else:
#         b = (10-(N%5))/2
#         a = (N-3*b-5)/5
#     return a,b
#
#
# def go(N):
#     if N%5 == 0:
#         return N/5,0
#     if (5-(N%5))%2 == 0:
#         b = (5-(N%5))/2
#         a = (N-3*b)/5
#     else:
#         b = (10-(N%5))/2
#         a = (N-3*b)/5
#     if a<0:
#         return -1
#     else:
#         return a+b