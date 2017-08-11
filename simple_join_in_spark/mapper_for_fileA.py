def split_fileA(line):
    # split the input line in word and count on the comma
    results = line.split(',')
    word = results[0]
    # turn the count to an integer
    count = int(results[1])
    return (word, count)
