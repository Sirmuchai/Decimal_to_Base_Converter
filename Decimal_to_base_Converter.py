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
    if c is not 2 or 8 or 16:     
        return print("Incorect base")
    a = base_converter(b,c)
    print(f"{b} to base 10 is {a} to base {c}")

verify(15,19)
        

        