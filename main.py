class Node:
    def __init__(self, name, deep, parent):
        self.childs = []
        self.parent = parent
        self.deep = deep
        self.name = name

    def addChild(self, child):
        self.childs.append(child)


def myRecursive(word, nodeList, stack, parent, deep):
    if len(word) is 0: #recursive bitisi
        return nodeList
    if len(stack)>0 and stack[0] is word[0]:  # stackte harf varsa
        deep -= 1
        newParent = None if deep is 0 else parent
        word = word[1:]
        nodeList = myRecursive(word, nodeList, stack, newParent, deep)
    else:
        nodeList[word[0]] = Node(word[1], parent, deep)
        deep += 1
        newParent = None if deep is 0 else word[0]
        word = word[2:]
        nodeList = myRecursive(word, nodeList, stack, newParent, deep)
    return nodeList


def printModel(stack):
    for elem in stack:
        print(int(stack[elem][2]) * "_" + elem, stack[elem][0], stack[elem][1])


if __name__ == '__main__':
    inputs = [
        "a2ab3f1fg2gb", "a2b1t4r7p1prtbac1x0xcm2m",
        "a2b1t4r7p1prtbac1x0xcm2f5fu5um",
        "g3a2b1t4r7p1prtbac1x0xcm2f5fu5umg"]
    for myWord in inputs:
        print("\n\n")
        st = myRecursive(word=myWord, nodeList={}, stack=[], parent=None, deep=0)
        printModel(st)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
