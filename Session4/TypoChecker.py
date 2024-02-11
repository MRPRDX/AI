def TypoChecker():
    inp = input().replace(".", " ").replace("!", " ").replace("'", "").split()
    correction = []
    strings = ""
    for i in range(len(inp)):
        words = []
        for j in range(len(inp[i])-4):
            if inp[i].isupper() != True:
                if len(inp) < 5:
                    words.append(inp[i][j:len(inp[i])].lower())
                else:
                    try:
                        words.append(inp[i][j:j+5].lower())
                    except:
                        pass
        for t in range(len(words)):
            if "a" not in words[t] and "o" not in words[t] and "u" not in words[t] and "e" not in words[t] and "i" not in words[t] and "y" not in words[t]:
                correction.append(inp[i])
    for items in correction:
        strings += items+" "
    return inp
print(TypoChecker(), end="")