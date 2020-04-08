#  https://atcoder.jp/contests/abc081/tasks/abc081_a

stringNumbers = list(input())

count = 0
for stringNum in stringNumbers:
    if stringNum == '1':
        count+=1

print(count)
