 #!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of ., ?, and :.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = [., ?, :]
    result = ""
    for char in text:
        result += char
        if char in punctuation:
            result += "\n\n"

    print(result.rstrip())
