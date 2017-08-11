def split_fileB(line):
    # split the input line into word, date and count_string
    results = line.split(' ')
    results2 = results[1].split(',')
    word = results2[0]
    date = results[0]
    count_string= results2[1]
    return (word, date + " " + count_string)