def sorter():
    inp = input().split()
    unsortedcap1 = []
    unsortedsmall1 = []
    char1listsmall = []
    char1listcap = []
    lis = []
    for i in inp:
        if i[0].isupper() == False:
            char1listsmall.append(ord(i[0]))
            unsortedsmall1.append(i.upper())
        else:
            char1listcap.append(ord(i[0]))
            unsortedcap1.append(i)
    zippedsmall1 = zip(char1listsmall, unsortedsmall1)
    zippedcap1 = zip(char1listcap, unsortedcap1)
    srtsmall1 = [x for _, x in sorted(zippedsmall1)]
    srtcap1 = [y for _, y in sorted(zippedcap1)]
    app = srtcap1 + srtsmall1
    app.sort()
    for k in range(len(app)):
        if app[k].isupper() == True:
            for p in range(k, len(app)):
                if app[p].isupper() == False:
                    if ord(app[p][0]) <= ord(app[k][0]):
                        if app[k] not in lis:
                            lis.append(app[k])
                            app[p], app[k] = app[k], app[p]
                            break
    for j in range(len(app)):
        if app[j].isupper() == True:
            app[j] = app[j].lower()
    # for p in range(len(app)):
    #     if
    strings = ''
    for items in app:
        if items != '0':
            strings += items+" "
    return strings
print(sorter())
