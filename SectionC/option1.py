"""Create a function that takes a numeral (just digits without separators (e.g. 19093 instead of 19,093) and 
returns the standard way of reading a number, complete with punctuation. """

d_unit = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
        6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine'}

d_en = {10 : 'ten', 11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
        15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
        19 : 'nineteen', 20 : 'twenty', 30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
        70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }

num = int(input("Please enter a numeric number: "))

def numeric_to_word(num):
   

    if num in d_unit:
        return d_unit.get(num)
    
    if num in d_en: 
        return d_en.get(num)
    

    ## ----  Tens ------"""
    if len(str(num))==2 and int(str(num)[0]) in d_unit and int(str(num)[1]) in d_unit:
        a = int(str(num)[0])
        for k,v in d_en.items():
            if int(str(k)[0]) == a:
                return v +" "+ d_unit.get(int(str(num)[1])) 
    
    ## -----Hundreds ------"""
    if len(str(num))==3:
        if str(num)[1:]==str("00"):
            return d_unit.get(int(str(num)[0])) +" "+ "hundred"  
        
        else:
            return d_unit.get(int(str(num)[0])) + " hundred" + " and "+  numeric_to_word(int(str(num)[1:]))
    
    ## -----Thousands ------"""
    elif len(str(num))==4:
        if str(num)[1:]==str("000"):
            return d_unit.get(int(str(num)[0])) +" "+ "thousand"  
        
        else:
            return d_unit.get(int(str(num)[0])) + " thousand" + " and "+  numeric_to_word(int(str(num)[1:]))
 
    ## ----Tens thousands ------"""
    elif len(str(num))==5:
        if str(num)[2:]==str("000"):
            return d_en.get(int(str(num)[0:2])) +" "+ "thousand"  
        
        else:
            return d_en.get(int(str(num)[0:2])) + " thousand" + " and "+  numeric_to_word(int(str(num)[2:]))
    
    ## ----hundred thousands ------"""   
    elif len(str(num))==6:
        if str(num)[3:]==str("000"):
            return numeric_to_word(int(str(num)[0:3])) +" "+ "thousand"  
        
        else:
            return numeric_to_word(int(str(num)[0:3])) + " thousand" + " "+  numeric_to_word(int(str(num)[3:]))
    
    ## ---- millions ------"""
    elif len(str(num))==7:
        if str(num)[1:]==str("000000"):
            return numeric_to_word(int(str(num)[0:1])) +" "+ "million"  
        
        else:
            return numeric_to_word(int(str(num)[0:1])) + " million" + " "+  numeric_to_word(int(str(num)[1:]))


if __name__=="__main__":
    numeric_to_word(num)

   
