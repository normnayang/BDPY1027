from itertools import chain ,combinations,permutations

result1= chain("abc","123",'甲乙丙')
print([t for t in result1])

result2 = combinations("abcd",2)
print([x for x in result2])

result3 = permutations("abcde",12)
l3 = [x for x in result3]

print(len(l3),l3)
