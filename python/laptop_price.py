cnt = int(input())
lis = []
for i in range(cnt):
    item = input().split()[:2]
    lis.append([int(item[0]), int(item[1])])

happy_irsa = False
for i in range(len(lis)):
    for j in range(len(lis)):
        if i != j:
            if lis[i][0] < lis[j][0] and lis[i][1] > lis[j][1]:
                happy_irsa = True
                break
    if happy_irsa:
        break

if happy_irsa:
    print('happy irsa')
else:
    print('poor irsa')
    
    