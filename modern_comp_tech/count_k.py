def main():
    print("Input string: ")
    string = str(input())
    words = string.lower().split()
    last_word = words[-1]    
    print(last_word.count("k"))

if __name__ == "__main__":
    main()
