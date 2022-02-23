def createColumn(columnNumbe):
    if columnNumbe < 27:
        return chr(64+columnNumbe)
    q, columnNumbe = divmod(columnNumbe, 26)
    if columnNumbe == 0:
        q -= 1
        columnNumbe = 26
    return createColumn(q) + chr(64+columnNumbe)


