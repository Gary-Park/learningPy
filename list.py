"""
    append(element)
    insert(index,element)
    extend

    del[리스트명(index)]
    pop(index)
    remove(value)

    전개연산자 *
"""

aList = [1,2,3,4,1,2,3,1,4,1,2,3,]
res_dict = {}

for i in range(0, len(aList)) :
    res_dict[i] = aList[i]

# for j in res_dict :
#     print ( j, ":", res_dict[j].i )
print ( res_dict.items() )

# print