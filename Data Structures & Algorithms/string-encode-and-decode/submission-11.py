class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            s += f'{len(i)}*#*{i}'

        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            num = i
            while  s[i].isnumeric():
                i += 1

            st = i + 3
            end = st + int(s[num:i])

            res.append(s[st:end])
            i = end
        return res
