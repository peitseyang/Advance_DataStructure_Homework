class TrieNode: 
    def __init__(self): 
        self.child = [None]*26
        self.isEndOfWord = False
  
class Trie: 
    def __init__(self): 
        self.root = self.getNode() 
  
    def getNode(self): 
        return TrieNode() 
  
    def char2Index(self, ch): 
        return ord(ch)-ord('a') 
  
    def insert(self, key):
        leaf = self.root
        for i in range(len(key)):
            idx = self.char2Index(key[i])
            if not leaf.child[idx]: 
                leaf.child[idx] = self.getNode() 
            leaf = leaf.child[idx] 
        leaf.isEndOfWord = True
  
    def search(self, key):
        leaf = self.root
        for i in range(len(key)): 
            idx = self.char2Index(key[i]) 
            if not leaf.child[idx]: 
                return False
            leaf = leaf.child[idx]
        return leaf != None and leaf.isEndOfWord

if __name__ == '__main__':
    # dir
    input_dir = './data/Compound Words.in'
    output_dir = './data/Compound Words.out'

    # create Trie
    dictionary = Trie()

    # insert words
    for line in open(input_dir, 'r').readlines():
        key = line.strip()
        if key == 'April' or key == 'December' or key == 'February' or key == 'Friday':
            continue
        dictionary.insert(key)
    
    # doc
    result = []

    # search Compound Words
    for line in open(input_dir, 'r').readlines():
        word = line.strip()
        if word == 'April' or word == 'December' or word == 'February' or word == 'Friday':
            continue
        for i in range(1, len(word)):
            sub_first = word[0:i]
            sub_second = word[i:len(word)]
            if dictionary.search(sub_first) and dictionary.search(sub_second):
                result.append(word)
                break

    # check accuracy
    ground_truth = open(output_dir, 'r').readlines()
    if len(result) != len(ground_truth):
        print('Result count inconsist')
    else:
        count = 0
        for i in range(len(result)):
            word = ground_truth[i].strip()
            if result[i] == word:
                count += 1
        if count == len(result):
            print('Match output file')
        else:
            print('Some error in result')

    # make output file
    filename = ''.join(['./', 'output.txt'])
    with open(filename, 'w') as f:
        for i in range(len(result)-1):
            f.write("%s\n" % result[i])
        f.write("%s" % result[len(result)-1])
    print('Output predict file...')
