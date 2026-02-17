def TextAnalyze(text=str):
    print()
    print("="*40)

    charsLen = len(text)
    words = str.split(text)

    if len(words) == 0:
        print("Вы ничего не вводили!")
        print("="*40)
        print()
        TextAnalyze(input("Напишите текст который надо Проанализировать: "))
        return
    
    sentences = 0

    longer = ""
    smaller = ""

    letters = 0
    uppercases = 0

    uniqueWords = []

    for word in words:
        wordLower = word.lower()
        if wordLower not in uniqueWords:
            uniqueWords.append(wordLower)
        
        if len(word) > len(longer):
            longer = word
        if smaller == "":
            smaller = word
        else:
            if len(word) < len(smaller):
                smaller = word

    for char in text:
        if char.isalpha():
            letters += 1
            if char.isupper():
                uppercases += 1
        if char in "!?.":
            sentences += 1
    
    uppercase = (uppercases / letters) * 100

    print()
    print(f"Общее количество символов: {charsLen}")
    print(f"Общее количество слов: {len(words)}")
    print(f"Общее количество предложений: {sentences}")
    print(f"Самое длинное слово: '{longer}' , Самое короткое: '{smaller}'.")
    print(f"Процент заглавных букв: {int(uppercase)}%")
    print(f"Уникальные слова: {uniqueWords}")
    print()
    print("="*40)

TextAnalyze(input("Напишите текст который надо Проанализировать: "))