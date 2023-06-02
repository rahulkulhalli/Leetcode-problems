class Solution:
    def isNumber(self, s: str) -> bool:
        def isValid(i_s, is_decimal_encountered=False, 
        is_sign_encountered=False, is_e_encountered=False, 
        is_num_encountered=False, currlen=0):
            if len(i_s) == 0:
                return True
            
            current_char = i_s[0]

            # Can't have +, - after . or after the first position.
            if current_char in ['+', '-']:
                if is_decimal_encountered:
                    return False
                if is_sign_encountered:
                    if not is_e_encountered:
                        return False
                if currlen > 0 and not is_e_encountered:
                    return False
                if currlen == len(s)-1:
                    return False
                if is_e_encountered:
                    if s[currlen-1].isnumeric():
                        return False
                
                return isValid(i_s[1:], is_decimal_encountered, True, is_e_encountered, is_num_encountered, currlen+1)

            # Can't have two decimals in a number
            if current_char == '.':
                if len(s) == 1:
                    return False
                if is_decimal_encountered:
                    return False
                if is_e_encountered:
                    return False
                if not is_num_encountered and currlen == len(s)-1:
                    return False
                
                
                return isValid(i_s[1:], True, is_sign_encountered, is_e_encountered, is_num_encountered, currlen+1)
            
            if current_char in ['e', 'E']:
                if is_e_encountered:
                    return False
                
                if is_decimal_encountered and s[0] == '.':
                    if not is_num_encountered:
                        return False
                
                if currlen == 0 or currlen == len(s)-1:
                    return False
                
                if not is_num_encountered:
                    return False
                
                return isValid(i_s[1:], is_decimal_encountered, is_sign_encountered, True, is_num_encountered, currlen+1)
            
            if current_char not in [str(i) for i in range(10)]:
                return False
            
            return isValid(i_s[1:], is_decimal_encountered, 
            is_sign_encountered, is_e_encountered, True, currlen+1)

        return isValid(s, False, False, False, 0)


if __name__ == "__main__":
    valids = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", "0", ".0e7"]
    for v in valids:
        print(f"{v}\t\t\t\t{Solution().isNumber(v)}")
    
    print(50*'-')
    
    non_valids = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", "e", ".", "4e+", "+.", "+E3", "092e359-2", "32.e-80123"]
    for nv in non_valids:
        print(f"{nv}\t\t\t\t{Solution().isNumber(nv)}")