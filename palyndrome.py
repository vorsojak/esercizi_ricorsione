
def palyndrome(word):
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and palyndrome(word[1:-1])

def palynfrome_banale(word):
    return word == word[::-1]

if __name__=="__main__":
    print(palyndrome("casa"))
    print(palynfrome_banale("osso"))