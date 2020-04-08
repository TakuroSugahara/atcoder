#  https://atcoder.jp/contests/abc069/tasks/abc069_b

strings = list(input())
str_len = len(strings)
print(strings[0] + str(str_len - 2) + strings[str_len - 1])
