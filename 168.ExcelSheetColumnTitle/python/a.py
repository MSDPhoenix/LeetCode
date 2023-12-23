"""

    FAIL

"""


# def convertToTitle(columnNumber):
#     alphabet = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
#     column_title = "x\n"
#     counter = columnNumber

#     def add_letters(column_title,columnNumber):
#         while columnNumber > 26:
#             print("columnNumberA",columnNumber)
#             column_title += alphabet[int((columnNumber-26)/26+1)]
#             columnNumber -= 26
#         column_title += alphabet[int(columnNumber%26)]
#         return column_title
#     column_title = add_letters(column_title,columnNumber)
#     print("columnNumberB",columnNumber)
#     return column_title

# print("0 --> ",convertToTitle(0),"\n")
# print("1 --> ",convertToTitle(1),"\n")
# print("2 --> ",convertToTitle(2),"\n")
# print("\n26 --> ",convertToTitle(26))
# print("\n27 --> ",convertToTitle(27))
# print("\n28 --> ",convertToTitle(28))
# print("\n701 --> ",convertToTitle(701))
# # print("\n702 --> ",convertToTitle(702))





def convertToTitle(columnNumber):
    alphabet = "ZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    title_end = alphabet[(columnNumber)%26]


    title_front = ""
    print("")
    while columnNumber >  26:
        print("columnNumber\t\t",columnNumber)
        
        print("(columnNumber%676-1)/26\t",int((columnNumber%676-1)/26))
        title_front += alphabet[int((columnNumber%676-1)/26)]

        columnNumber -= 676

    return title_front + title_end

print("1 --> ",convertToTitle(1))
print("2 --> ",convertToTitle(2))
print("26 --> ",convertToTitle(26))
print("*")
print("27 --> ",convertToTitle(27))
print("28 --> ",convertToTitle(28))
print("51 --> ",convertToTitle(51))
print("52 --> ",convertToTitle(52))
print("*")
print("53 --> ",convertToTitle(53))
print("78 --> ",convertToTitle(78))
print("*")
print("79 --> ",convertToTitle(79))
print("104 --> ",convertToTitle(104))
print("*")
print("105 --> ",convertToTitle(105))
print("130 --> ",convertToTitle(130))
print("*")
print("676 --> ",convertToTitle(676))
print("*")
print("677 --> ",convertToTitle(677))
print("701 --> ",convertToTitle(701))
print("702 --> ",convertToTitle(702))
print("*")
print("703 --> ",convertToTitle(703))
print("728 --> ",convertToTitle(728))
print("*")
print("729 --> ",convertToTitle(729))
# print("754 --> ",convertToTitle(754))
print("*")
print("*")
print("")

