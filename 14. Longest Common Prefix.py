class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortestString = min(strs, key=len)
        longestPrefix = strs[0][:len(shortestString)]
        p_leng = 0

        for i in range(len(shortestString)):
            for k in range(len(strs)):
                if longestPrefix[i] != strs[k][i]:
                    return longestPrefix[:p_leng]
            p_leng+=1
        print("longestPrefix", longestPrefix, "longestPrefix[:p_leng]", longestPrefix[:p_leng])

        return longestPrefix[:p_leng]

