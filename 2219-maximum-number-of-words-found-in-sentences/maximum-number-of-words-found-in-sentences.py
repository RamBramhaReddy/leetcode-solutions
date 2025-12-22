class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        for s in sentences:
            word_count = len(s.split())   
            if word_count > max_words:
                max_words = word_count

        return max_words