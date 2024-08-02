#Trie, O(N) preprocessing and O(N) space complexity

#a Trie works basically as a adjacencylist/tree, where each node points to another node for words, and stops once there is a "True", indicating a full word

#Basically, it checks words by traversing the adjacency list, and it builds the trie by leaving pointers

#It is imperative that it leaves pointers only when there hasn't been one before, and it it leaves pointers at the current end of the list

trielist = [[[-1]*26,False]]

def addstring(string,triearr):
    indextracker = 0
    for character in string:
        characternum = ord(character)-ord('a')
        if triearr[indextracker][0][characternum]==-1:
            triearr[indextracker][0][characternum] = len(triearr)
            triearr.append([[-1]*26,False])
        indextracker = triearr[indextracker][0][characternum]
    triearr[indextracker][1]=True

def stringchecker(string,triearr):
    indextracker = 0
    for char in string:
        charindex = ord(char)-ord('a')
        if triearr[indextracker][0][charindex]==-1:
            return False
        indextracker = triearr[indextracker][0][charindex]
    return triearr[indextracker][1]