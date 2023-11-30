N = int(input())
ans = []
for _ in range(N):
    parenthesis = input()
    stack = []

    for c in parenthesis:
        if len(stack) == 0:
            if c == ')':
                stack.append(c)
                break
            else:
                stack.append(c)
        else:
            if stack[-1] == '(' and c == ')':
                stack.pop()
            else:
                stack.append(c)

    if len(stack) == 0:
        ans.append('YES')
    else:
        ans.append('NO')

for i in ans:
    print(i)
