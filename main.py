def first_word(text):

    text = text.lstrip(' .,')

    first_word_start = -1
    first_word_end = -1

    for i, char in enumerate(text):
        if char.isalpha() or char == "'":
            if first_word_start == -1:
                first_word_start = i
            first_word_end = i
        elif first_word_start != -1:
            break

    return text[first_word_start:first_word_end + 1]

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')