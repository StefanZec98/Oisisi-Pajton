class TrieNode(object):

    def __init__(self, char = str):
        self.char = char
        self.children = []                #lista reci
        self.kraj_reci = False       #gledamo da li je poslednji
        self.counter = 0
        self.recnik = {}             #ovde smestamo reci koje pretrazimo

def add(root, word = str, html_word = str):
    node = root
    word_len = len(word)
    for char in word:
        word_len -= 1
        found_in_child = False
        for child in node.children:      #trazimo karakter u cvoru
            if child.char == char:
                node = child             #vezi cvor i karakter
                found_in_child = True
                break
        if not found_in_child:           #ako ne nadjemo karakter, trebamo ga napraviti
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node              #vezi cvor i karakter
    node.kraj_reci = True                #kraj reci
    if(html_word in node.recnik.keys()):
        node.recnik[html_word] += 1
    else:
        node.recnik[html_word] = 1
    node.counter += 1
    return node.counter

def trazi_rec(root, word = str):
    node = root
    if not root.children:               #ako cvor nema karakter, tj ako je prazan
        return False, 0
    for char in word:
        char_not_found = True
        for child in node.children:     #pretrazi karaktere trenutnog cvora
            if child.char == char:
                char_not_found = False
                node = child
                break
        if char_not_found:
                return False, 0
        if node.kraj_reci == False:
            node.counter = 0
    return node.kraj_reci, node.counter, node.recnik    #ako pronadjemo rec, vrati True i broj pronalazenja date reci

'''                             ova funkcija trazi i koren reci u stablu
def find_prefix(self, prefix):
    """
    Check and return
      1. If the prefix exists in any of the words we added so far
      2. If yes then how may words actually have the prefix
    """
    node = self.root
    # If the root node has no children, then return False.
    # Because it means we are trying to search in an empty trie
    if not self.root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        # Search through all the children of the present node
        for child in node.children:
            if child.char == char:
                # We found the char existing in the child.
                char_not_found = False
                # Assign node as the child containing the char and break
                node = child
                break
        # Return False anyway when we did not find a char.
        if char_not_found:
            return {}
    # Well, we are here means we have found the prefix. Return true to indicate that
    # And also the counter of the last node. This indicates how many words have this
    # prefix
    return node.counter
'''

'''
if _name_ == "_main_":
    trie = TrieNode('o')
    add(trie, "nemanja")
    add(trie, 'stefan')

    # print(find_prefix('pree'))
    # print(find_prefix('prefiks'))
'''