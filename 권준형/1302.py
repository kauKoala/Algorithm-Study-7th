# 1302 베스트셀러
book_d = {}
for i in range(int(input())):
    st = input()
    if book_d.get(st):
        book_d[st] += 1
    else:
        book_d[st] = 1
m = max(book_d.values())
most = sorted([key for key in book_d if book_d[key] == m])
print(most[0])
