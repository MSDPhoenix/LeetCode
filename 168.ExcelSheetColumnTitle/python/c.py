def convertToTitle(columnNumber):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    title = ""
    while columnNumber > 0:
        columnNumber -= 1
        title = alpha[columnNumber%26] + title
        columnNumber //= 26
    return title



print("1 --> ",convertToTitle(1)) # A
    # column number 1 -> 0 , title = chr(65+0)..., 0//26 = 0
print("2 --> ",convertToTitle(2))
    # column number 2 -> 1 , title = chr(65+1)..., 1//26 = 0
print("3 --> ",convertToTitle(3))
print("4 --> ",convertToTitle(4))
print("5 --> ",convertToTitle(5))
print("6 --> ",convertToTitle(6))
print("25 --> ",convertToTitle(25))
print("26 --> ",convertToTitle(26)) # Z
    # column number 26 -> 25 , title = chr(65+25)..., 25//26 = 0
print("\n*")
print("27 --> ",convertToTitle(27))# AA
    # column number 27 -> 26 , title = chr(65+0)..., 26//26 = 1
    # column number 1 -> 0 , title = chr(65+0)..., 0//26 = 0
print("28 --> ",convertToTitle(28))
    # column number 28 -> 27 , title = chr(65+1)..., 27//26 = 1
    # column number 1 -> 0 , title = chr(65+0)..., 0//26 = 0
print("51 --> ",convertToTitle(51))
print("52 --> ",convertToTitle(52)) # AZ
    # column number 52 -> 51 , title = chr(65+25)..., 51//26 = 1
    # column number 1 -> 0 , title = chr(65+0)..., 0//26 = 0
print("\n*")
print("53 --> ",convertToTitle(53)) # BA
    # column number 53 -> 52 , title = chr(65+0)..., 52//26 = 2
    # column number 2 -> 1 , title = chr(65+1)..., 2//26 = 0
print("78 --> ",convertToTitle(78)) # BZ
print("\n*")
print("79 --> ",convertToTitle(79))
print("104 --> ",convertToTitle(104)) # BZ
print("\n*")
print("105 --> ",convertToTitle(105))
print("130 --> ",convertToTitle(130)) # CZ
print("\n*")
print("676 --> ",convertToTitle(676)) # YZ
print("\n*")
print("677 --> ",convertToTitle(677)) # ZA
print("701 --> ",convertToTitle(701)) # ZY
print("702 --> ",convertToTitle(702)) # ZZ
print("\n*")
print("703 --> ",convertToTitle(703)) # AAA
    # column number 703 -> 702 , title = chr(65+0)..., 702//26 = 27
    # column number 27 -> 26 , title = chr(65+0)..., 26//26 = 1
    # column number 1 -> 0 , title = chr(65+0)..., 0//26 = 0
print("728 --> ",convertToTitle(728)) # 
print("\n*")
print("729 --> ",convertToTitle(729))
print("754 --> ",convertToTitle(754))
print("\n*")
print("18278 --> ",convertToTitle(18278))
print("18279 --> ",convertToTitle(18279))
print("\n*")
print("475254 --> ",convertToTitle(475254))
print("475255 --> ",convertToTitle(475255))
print("\n*")
print("12356630 --> ",convertToTitle(12356630))
print("12356631 --> ",convertToTitle(12356631))
print("*")

print(702//26)

# print(26**5 + 475254)