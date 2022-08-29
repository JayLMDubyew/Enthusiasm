
def array_intersections(arra, arrb):
    #O(N) time
    flappymappy = {}
    intersection = []
    for i in arra:
        flappymappy[i] = True
    for i in arrb:
        if(i in flappymappy):
            intersection.append(i)
    return intersection


def findthedupe(arrc):
    #also O(N)
    hashymcmappy = {}
    for i in arrc:
        if i in hashymcmappy:
            return i
        else:
            hashymcmappy[i] = True


arra = [1, 2, 3, 4]
arrb = [2, 4, 6, 8]
print(array_intersections(arra, arrb))

letterz = ['a', 'b', 'c', 'd', 'a', 'f']
print(findthedupe(letterz))

