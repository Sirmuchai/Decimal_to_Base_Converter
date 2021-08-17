"""
Given a cerian value in decimal convert the number to either Binary (base 2)
Octal (base 8) or Hexadecimal(base 16)
"""
def base_converter(dec_num, base):
    bits = "0123456789ABCDEF"
    result = []        
    #loop for division to get the reminder
    while dec_num > 0:
        rem = dec_num % base
        result.append(rem)
        dec_num //=base
    #loop to get the reminders from the last
    final_results = ""
    while result > []:
        bit = result.pop()
        final_results = final_results + bits[bit]
        
    return final_results

#method to display output
def verify(b,c):
    if (c ==2 or c ==8 or c==16):
        a = base_converter(b,c)
        return print(f"{b} to base 10 is {a} to base {c}")
    else:
         return print("Incorect base")

#Examples to verify        
verify(15,19)
verify(333,16)
verify(15,8)
verify(201,2)
        

        
