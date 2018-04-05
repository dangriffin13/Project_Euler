import math

t = int(input())

def three_digit_handler(num):
    if num >= 100:
        return d[num//100] + ' Hundred ' + str(three_digit_handler(num%100))
    elif num % 10 == 0 or num < 20:
        return d[num]
    else:
        return d[num//10*10] + ' ' + three_digit_handler(num%10)
        

d = {0: '', 1: 'One', 2: 'Two', 3:'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
    10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 
    15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen',18: 'Eighteen',19: 'Nineteen', 
    20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',60: 'Sixty', 70: 'Seventy', 80: 'Eighty',90: 'Ninety',
}

illions = {1: '', 2: 'Thousand', 3: 'Million', 4: 'Billion', 5: 'Trillion'}

for _ in range(t):
    n = int(input())
    
    if n == 0:
        print('Zero')
        
    else:
        digits = list(str(n))
        if len(digits) < 3:
            print(three_digit_handler(int(''.join(digits[0:]))))
        else:
            offset = len(digits) % 3
            illion_counter = math.ceil(len(digits)/3)
            
            if offset != 0:  #if string isn't divisible by 3, start with those leading digits
                value = int(''.join(digits[0:offset]))
                word = three_digit_handler(value) + ' ' + illions[illion_counter] + ' '
                illion_counter -= 1
            else:
                word = ''

            
            for i in range(illion_counter): #check three digits at a time and append unit names
                value = int(''.join(digits[offset+(i*3):offset+(i*3)+3]))
                if value == 0:
                    word = word
                else:
                    word = word + three_digit_handler(value).rstrip() + ' ' + illions[illion_counter] + ' '
                illion_counter -= 1
            

            print(word.rstrip())