def romanToInt(s: str) -> int:
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    
    for i in range(len(s)):
        if i > 0 and roman_map[s[i]] > roman_map[s[i - 1]]:
            result += roman_map[s[i]] - 2 * roman_map[s[i - 1]]
        else:
            result += roman_map[s[i]]
    
    return result
    
print(romanToInt("III"))      
print(romanToInt("LVIII"))     
print(romanToInt("MCMXCIV"))   
