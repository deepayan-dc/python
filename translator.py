def translate (string):
    translation = ""
    for letter in string:
        if letter in "AEIOUaeiou":
            translation = translation + "d"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))