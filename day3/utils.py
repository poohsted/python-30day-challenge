def safe_divide(a, b):
    """Safely divide two numbers. Returns None if division by zero"""
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None

def capitalize_words(sentence):
    """Capitalize the first letter of each word in a sentence."""
    return ' '.join(word.capitalizate() for word in sentence.split())
