def romanToInt(self, s: str) -> int:
    dic = {"I" : 1, "V": 5, "X":10, "L": 50, "C": 100, "D": 500, "M": 1000}
    dic2 = {"V": "I","X": "I","L": "X","C": "X","D": "C","M": "C",}
    num = 0

    array = list(enumerate(s))
    for i, char in array:
        if(dic.get(char) is not None ):
            NumeroConvertido = dic[char]
            if(i + 1 <= len(array) and s[i+1] is not None ):
                nextNum = s[i+1]
            else:
                nextNull = None

            if (dic2.get(nextNum) is not None and nextNull is not None):
                num -= NumeroConvertido
            else:
                num += NumeroConvertido

            # x = i 
            # next = v


            # I ANTE DE V E X
            # X ANTES DE L E C
            # C ANTES DE D E M
            

            # I ANTES DO V = 4 E I ANTES DO X= 9

        

    return num