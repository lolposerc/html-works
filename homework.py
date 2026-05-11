def text_analyzer(text):
    total_chars = len(text)
    
    space_count = text.count(' ')
    
    digit_count = 0

    for char in text:
        if char.isdigit():
            digit_count += 1

    uppercase_count = 0

    for char in text:
        if char.isupper():
            uppercase_count += 1
    
    lowercase_count = 0

    for char in text:
        if char.islower():
            lowercase_count += 1
    
    words = text.split()
    total_words = len(words)
    
    most_common_list = {}
    most_common_word = ''
    most_common_max_count = 0
    
    for word in words:
        if word in most_common_list:
            most_common_list[word] += 1
        else:
            most_common_list[word] = 1
        
        if most_common_list[word] > most_common_max_count:
            most_common_max_count = most_common_list[word]
            most_common_word = word
    
    result = {
        'total_chars': total_chars,
        'total_words': total_words,
        'uppercase_count': uppercase_count,
        'lowercase_count': lowercase_count,
        'digit_count': digit_count,
        'space_count': space_count,
        'most_common_word': most_common_word
    }
    
    return result


text = 'Hello World! Hello Python. Python 3.9'
result = text_analyzer(text)
print(result)
