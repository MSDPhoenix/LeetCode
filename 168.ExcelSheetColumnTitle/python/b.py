"""

    FAIL

"""




# the first 26^ = 26 columns produce one letter
# the next 26^2 = 676 columns produce two letters
# the next 26^3 = 17576 columns produce three letters
# the next 26^4 = 456,976 columns produce four letters
# the next 26^5 = 11,881,376 columns produce four letters

# start by getting the number of letters in the column name right, then figure out what those letters should be

def convertToTitle(columnNumber):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZA"
    factor = 26
    count = columnNumber-26
    exponent = 0
    title = "...."

    print("")
    while count > 0:
        print("count\t",count)
        print("factor\t",factor)
        print("((count -1)/factor) o/o factor\t",((count-1)/factor)%factor)
        string_index = int((count-1)/factor)%factor

        # for columns 27-52, string_index should be 0
        print("string_index\t",string_index)
        title = alphabet[string_index] + title
        
        
        factor*=26
        count -= factor
    return title



        # count increments by 1 for 1-26        = (26^0) + 0
            # then 26 for 27-702                = (26^1) + 0 + 26
            # then 676 for 703-18278 (26**3)    = (26^2) + 26 + 702
        
            # increment = 26^exponent
            # count += increment
        
        # exponent starts as 0
            # exponent = 0 for 1-26
            # exponent = 1 for 27-702
            # exponent = 2 for 703-18278
        
            # exponent += 1

        # factor starts as 1 for 1-26       = 
            # factor = 26 for 27-702        = 
            # factor = 676 for 703-18278    = 
        
            # factor = factor + 26^exponent 
        
        
        # list index = 0 for column 1       = (( 1-0) -1 ] / 1 )         = (        ) 
        # list index = 25 for column 26     = (( 26-0) -1 ] / 1 )        = (        ) 

        # list index = 0 for column 27       = (( 27 - 26) -1 ]/ 26 )     
        # list index = 0 for column 52       = (( 52 - 26) -1 ]/ 26 )    
        # list index = 1 for column 53       = (( 53 - 26) -1 ]/ 26 )    
        # list index = 1 for column 78       = (( 78 - 26) -1 ]/ 26 )    
        # list index = 2 for column 79       = (( 79 - 26) -1 ]/ 26 )    
        # list index = 2 for column 104      = (( 104 - 26) -1 ]/ 26 )   
        # list index = 24 for column 676     = (( 676 - 26) -1 ]/ 26 )   
        # list index = 25 for column 677     = (( 677 - 26) -1 ]/ 26 )   
        # list index = 25 for column 702     = (( 702 - 26) -1 ]/ 26 )   

        # list index = 0 for column 703      = (( 703 - 702) -1 ]/ 702 )    
        # list index = 0 for column 1404      = (( 1404 - 702) -1 ]/ 702 )    
        # list index = 1 for column 1405      = (( 1405 - 702) -1 ]/ 702 )    
        # list index = 1 for column 2106      = (( 2106 - 702) -1 ]/ 702 )    
        # list index = 2 for column 2107      = (( 2107 - 702) -1 ]/ 702 )    
        # list index = 24 for column 17576   = (( 17576 - 702) -1 ]/702 )    
        # list index = 25 for column 18278   = (( 18278 - 702) -1 ]/702 )    

        # list index = 0 for count 17603    = (( 17603) -1 ]/17603 )    % 26

            # list index = ( count -1 )/
        
        # factor starts as 1 then 26, then 676, then 
    
        


print("1 --> ",convertToTitle(1))
print("2 --> ",convertToTitle(2))
print("3 --> ",convertToTitle(3))
print("4 --> ",convertToTitle(4))
print("5 --> ",convertToTitle(5))
print("6 --> ",convertToTitle(6))
print("25 --> ",convertToTitle(25))
print("26 --> ",convertToTitle(26)) # AA
print("\n*")
print("27 --> ",convertToTitle(27))
print("28 --> ",convertToTitle(28))
print("51 --> ",convertToTitle(51))
print("52 --> ",convertToTitle(52)) # AZ
print("\n*")
print("53 --> ",convertToTitle(53)) # BA
print("78 --> ",convertToTitle(78)) # BZ
print("\n*")
print("79 --> ",convertToTitle(79))
print("104 --> ",convertToTitle(104))
print("\n*")
print("105 --> ",convertToTitle(105))
print("130 --> ",convertToTitle(130))
print("\n*")
print("676 --> ",convertToTitle(676))
print("\n*")
print("677 --> ",convertToTitle(677))
print("701 --> ",convertToTitle(701))
print("702 --> ",convertToTitle(702))
print("\n*")
print("703 --> ",convertToTitle(703))
print("728 --> ",convertToTitle(728))
print("\n*")
print("729 --> ",convertToTitle(729))
print("754 --> ",convertToTitle(754))
print("\n*")
print("18278 --> ",convertToTitle(18278))
print("18279 --> ",convertToTitle(18279))
print("\n*")
print("475228 --> ",convertToTitle(475228))
print("475229 --> ",convertToTitle(475229))
print("\n*")
print("12355928 --> ",convertToTitle(12355928))
print("12355928 --> ",convertToTitle(12355928))
print("*")
# print("*")
# print("")

# 702 --> letter index = int(count-1)/factor = 701/26 = 26
# 703 --> letter index = int(count-1)/factor = 702/26 = 27