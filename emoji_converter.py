def convert(message):
    words = message.split(' ')
    emojis = {
        ":)": "😀",
        ":(": "🙁",
        ":|": "😐"             # windows: windows + .
    }
    output = ''
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("> ")
print(convert(message))