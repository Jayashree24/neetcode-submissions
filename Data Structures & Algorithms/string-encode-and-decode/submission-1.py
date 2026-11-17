class Solution:

    def encode(self, strs: List[str]) -> str:
        k = ''
        for s in strs:
            k += '/?' + s
        return k


    def decode(self, s: str) -> List[str]:
        return s.split("/?")[1:]
