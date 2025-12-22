class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        n =set()
        for i in sentence:
            n.add(i)
        return len(n) == 26