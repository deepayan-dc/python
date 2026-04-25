def translate (string):
    translation = ""
    for letter in string:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "D"
            else:
                translation = translation + "d"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))