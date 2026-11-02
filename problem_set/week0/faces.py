def convert(text):
    text = str.replace(":)","🙂")
    text = str.replace(":(", "🙁")
    return text

def main():
    print(convert(input("Enter your text: ")))

main()