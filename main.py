BOOKPATH = 'books/frankenstein.txt'


def readBook(bookPath):
    with open(bookPath) as f:
        return f.read()


def count_words():
    return len(readBook(BOOKPATH).split())


def count_letters():
    bookContent = readBook(BOOKPATH).lower()
    letter_counts = {}
    for letter in bookContent:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts


def bookReport(bookPath):
    wordCount = count_words()
    letter_count = count_letters()
    print(f" --- Begin report of {bookPath} ---")
    print(f" {wordCount} words found in the document")
    for letter in dict(sorted(letter_count.items(), reverse=True, key=lambda item: item[1])):
        print(f"The {letter} character was found {
              letter_count[letter]} times.")
    print(' --- END REPORT --- ')


if __name__ == '__main__':
    bookReport(BOOKPATH)
