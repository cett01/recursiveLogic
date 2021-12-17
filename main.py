class Node:
    def __init__(self, name, value, deep, parent):
        self.children = []
        self.deep = deep
        self.name = name
        self.value = value
        self.parent = parent

    def addChild(self, child):
        self.children.append(child)

    def sortChilds(self):
        if len(self.children) > 0:  # eğer ki çocugu varsa value değerine göre sıralama yapıyorum.
            # Eğer ki valuelar eşit olursa da indexinde göre ters sıralama yapıyorum.
            # Bu da bana BFS olarak son eklenen elemanı önce yazdırmamı sağlıyor.
            return sorted(self.children, key=lambda x: (x.value, -self.children.index(x)))
        return []


def myRec(word, node: Node, st: [], deep: int):
    if len(word) is 0:  # recursive bitisi
        return node
    character = word[0]  # ilk elemanı alıyorum

    if next((x for x in st if x.name == character), None):  # eger ki stackte eleman varsa deep bitişi demektir
        st.pop()  # stackten elemanımı çektim
        word = word[1:]  # kelimeden bitiş harfini çıkardım.
        deep -= 1  # üst levele çıkıyorum.
        node = myRec(word, node.parent, st, deep)  # recursive methoda girecek ve dönüş değerim bana parentı verecek.
    else:  # stackte eleman yoksa yeni eleman eklemem lazım
        deep += 1  # deep arttırdım alt levele geçiyoruz.
        value = word[1]  # sayıyı aldım
        newNode = Node(character, value, deep, node)  # yeni nodu oluşturdum.
        node.addChild(newNode)  # yeni nodu parentın çocuğu olarak ekledim
        word = word[2:]  # aldığım harfleri kelimeden çıkardım
        st.append(newNode)  # elemanımı stacke ekledim
        node = myRec(word, newNode, st,
                     deep)  # recursive olarak tekrar aynı işlemi yapmasını istedim. dönüş değeri parent elemanımı versin istiyorum.
    return node


def printNode(node):
    print("_" * (
                node.deep - 1) + node.name)  # burada 0. level benim işlevsiz Node'um oldugu için deep-1 den başlayarak yazdırdım.
    for child in node.sortChilds():  # çocukları value ve eklenme sırasına göre BFS olarak sıralayarak print ediyorum.
        printNode(child)  # burada da recursive olarak çalışmak durumunda.


if __name__ == '__main__':
    inputs = [
        "a2ab3f1fg2gb",
        "a2b1t4r7p1prtbac1x0xcm2m",
        "a2b1t4r7p1prtbac1x0xcm2f5fu5um",
        "g3a2b1t4r7p1prtbac1x0xcm2f5fu5umg"
    ]

    for myWord in inputs:
        print("\n\n")
        st = myRec(word=myWord, node=Node("", 0, 0, None), st=[],
                   deep=0)  # kelimemi, işlevsiz Parent Node'u, Stack Listemi ve sıfır derinliği gönderiyorum.
        # sonuç olarak bana Parent Node dönmesini bekliyorum.
        printNode(st)  # yazdırma işlemi burada gerçekleşiyor

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
