class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_FOUND = '$'
        
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node
                node = node.setdefault(letter, {})
            # the word exists
            node[WORD_FOUND] = word
            
        rowNum = len(board)
        colNum = len(board[0])
        
        matchedWords = []
        
        # backtracking, use the hashset data structure from Python
        def backtracking(row, col, parent):
            letter = board[row][col]
            currNode = parent[letter]
            
            # find a match
            word_match = currNode.pop(WORD_FOUND, False)
            if word_match:
                matchedWords.append(word_match)

            board[row][col] = '#' # we visited the letter already

            # explore the neighboring cells
            for (rowNext, colNext) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row+rowNext, col+colNext
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)
            
            board[row][col] = letter
            
            # remove the matched leaf node in Trie
            if not currNode:
                parent.pop(letter)
        
        for row in range(rowNum):
            for col in range(colNum):
                if board[row][col] in trie:
                    backtracking(row, col, trie)
                    
        return matchedWords
        