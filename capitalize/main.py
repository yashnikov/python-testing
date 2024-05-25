def capitalize(text):
    if not text:  # Check if the text is empty
        return text
    first_char, *rest_chars = text
    rest_substring = ''.join(rest_chars)
    return f'{first_char.upper()}{rest_substring}'


capitalize('hello, hexlet!')