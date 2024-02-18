def count_agtc(dna):
    return dna.count("A"), dna.count('T'),dna.count('G'), dna.count('C')
print(count_agtc('tydydjtyDGTHTRHTHTYjtyjtfjtytytyjty'))

def is_palindrome(text):
    text1 = text.lower()
    text2 = ''
    for char in text1:
        if char.isalpha():
            text2 += char
    return text2 == text2[::-1]


text = 'hkdj . gfkj'
print(is_palindrome(text))