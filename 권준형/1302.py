# 1302 베스트셀러
book_d = dict()
for _ in range(int(input())):
    st = input()
    if st in book_d:
        book_d[st] += 1
    else:
        book_d[st] = 1
print(sorted(book_d.items(), key=lambda x :(-x[1], x[0]))[0][0])
