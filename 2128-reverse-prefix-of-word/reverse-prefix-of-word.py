class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        s1 = ""
        s2 = ""
        lim = 0
        for i in range(len(word)):
            if word[i] == ch:
                lim = i
                break
        for i in word:
            if ch not in word:
                print(word)
        for i in range(lim+1):
            s1 = s1 + word[i]
        s2 = s1[::-1]
        for i in word[lim+1:len(word)]:
            s2 = s2+i
        return s2