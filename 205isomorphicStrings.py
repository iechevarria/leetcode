class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sd = {}
        td = {}
        for i in range(len(s)):
            if s[i] in sd:
                sd[s[i]] += [i]
            else:
                sd[s[i]] = [i]
            if t[i] in td:
                td[t[i]] += [i]
            else: 
                td[t[i]] = [i]
    
        return sorted(sd.values()) == sorted(td.values())

    def isIsomorphicAlt(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(zip(s,t))) == len(set(s)) == len(set(t)) 
        