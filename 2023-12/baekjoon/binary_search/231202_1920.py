N = int(input())
n_list = list(map(int, input().split()))
M = int(input())
m_list = list(map(int, input().split()))
ans_list = []

n_list.sort()
for i in range(M):
    left_index = 0
    right_index = len(n_list) - 1

    target_num = m_list[i]
    flag = True

    while left_index <= right_index:
        mid = (left_index + right_index) // 2
        if target_num == n_list[mid]:
            print(1)
            flag = False
            break
        elif target_num > n_list[mid]:
            left_index = mid + 1
        else:
            right_index = mid - 1
    if flag:
        print(0)
