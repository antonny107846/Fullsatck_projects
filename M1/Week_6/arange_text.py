def arange_words(text):
    word_list = text.split('-')  
    word_list.sort() 
    result = '-'.join(word_list)  
    return result

text = "python-variable-funcion-computadora-monitor"
result = arange_words(text)
print(result)  
